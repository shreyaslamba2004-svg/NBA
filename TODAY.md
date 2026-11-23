# NBA model · Mon 23 Nov 2026 (US date)

Updated **Mon 23 Nov, 05:24 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-23/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes PA over 44.5 (45+) | MIL @ TOR | draftkings | 17.00 | 14.37 | 6.66 | 15.0% | 5.5% | 7.0% | +18.4% | +155.1% | 0.3% |
| Scottie Barnes PRA over 54.5 (55+) | MIL @ TOR | draftkings | 17.80 | 15.46 | 7.58 | 13.2% | 5.2% | 6.5% | +15.2% | +134.7% | 0.2% |
| Trey Murphy III AST over 5.5 (6+) | PHX @ NOP | draftkings | 11.80 | 10.52 | 5.48 | 18.3% | 7.9% | 9.5% | +12.2% | +115.4% | 0.3% |
| Ryan Kalkbrenner REB over 9.5 (10+) | MEM @ CHA | draftkings | 19.80 | 17.92 | 9.70 | 10.3% | 4.7% | 5.6% | +10.5% | +104.2% | 0.1% |
| Scottie Barnes PRA over 49.5 (50+) | MIL @ TOR | draftkings | 9.10 | 8.25 | 4.49 | 22.3% | 10.3% | 12.1% | +10.3% | +102.5% | 0.3% |
| Scottie Barnes PA over 39.5 (40+) | MIL @ TOR | draftkings | 7.70 | 7.04 | 3.92 | 25.5% | 12.1% | 14.2% | +9.3% | +96.5% | 0.4% |
| Scottie Barnes PR over 49.5 (50+) | MIL @ TOR | draftkings | 20.80 | 19.05 | 10.64 | 9.4% | 4.5% | 5.2% | +9.2% | +95.5% | 0.1% |
| Cam Spencer AST over 11.5 (12+) | MEM @ CHA | draftkings | 29.00 | 26.60 | 14.83 | 6.7% | 3.2% | 3.8% | +9.2% | +95.6% | 0.1% |
| Cam Spencer AST over 9.5 (10+) | MEM @ CHA | draftkings | 11.80 | 10.86 | 6.14 | 16.3% | 7.9% | 9.2% | +8.6% | +92.1% | 0.2% |
| Scottie Barnes AST over 11.5 (12+) | MIL @ TOR | draftkings | 26.00 | 23.98 | 13.62 | 7.3% | 3.6% | 4.2% | +8.5% | +90.8% | 0.1% |
| Scottie Barnes AST over 9.5 (10+) | MIL @ TOR | draftkings | 10.20 | 9.44 | 5.43 | 18.4% | 9.2% | 10.6% | +8.0% | +87.9% | 0.2% |
| Scottie Barnes PR over 44.5 (45+) | MIL @ TOR | draftkings | 10.80 | 10.10 | 5.98 | 16.7% | 8.6% | 9.9% | +6.9% | +80.5% | 0.2% |
| Ryan Kalkbrenner REB over 7.5 (8+) | MEM @ CHA | draftkings | 7.70 | 7.22 | 4.28 | 23.4% | 12.1% | 13.9% | +6.8% | +79.8% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MEM @ CHA | Tue 24 Nov 11:00 | 111.0–110.1 | MEM 52% | 1.91 / 2.10 | CHA +1.5 | 221.5 | CHA +3.5 covers 57%; o215.5 61% |
| POR @ PHI | Tue 24 Nov 11:00 | 114.7–116.2 | POR 46% | 2.17 / 1.85 | PHI -1.5 | 230.5 | PHI -3.5 covers 45%; o231.5 48% |
| OKC @ IND | Tue 24 Nov 11:30 | 117.5–112.7 | OKC 63% | 1.58 / 2.73 | IND +4.5 | 230.5 | IND +4.5 covers 49%; o222.5 66% |
| MIL @ TOR | Tue 24 Nov 11:30 | 107.2–116.2 | MIL 26% | 3.86 / 1.35 | TOR -8.5 | 223.5 | TOR -10.5 covers 46%; o223.5 50% |
| BKN @ MIN | Tue 24 Nov 11:30 | 105.6–115.5 | BKN 24% | 4.13 / 1.32 | MIN -10.5 | 220.5 | MIN -12.5 covers 43%; o223.5 44% |
| CLE @ CHI | Tue 24 Nov 12:00 | 124.3–117.1 | CLE 69% | 1.45 / 3.24 | CHI +7.5 | 241.5 | CHI +8.5 covers 53%; o239.5 53% |
| PHX @ NOP | Tue 24 Nov 12:00 | 121.6–115.6 | PHX 67% | 1.50 / 2.99 | NOP +6.5 | 237.5 | NOP +3.5 covers 42%; o233.5 57% |
| LAC @ HOU | Tue 24 Nov 12:30 | 108.7–118.0 | LAC 26% | 3.92 / 1.34 | HOU -9.5 | 226.5 | HOU -12.5 covers 41%; o225.5 52% |
| UTA @ LAL | Tue 24 Nov 14:00 | 109.1–123.9 | UTA 14% | 6.98 / 1.17 | LAL -14.5 | 232.5 | LAL -13.5 covers 54%; o228.5 59% |
| SAS @ SAC | Tue 24 Nov 14:00 | 116.7–108.9 | SAS 71% | 1.41 / 3.43 | SAC +7.5 | 225.5 | SAC +10.5 covers 58%; o224.5 52% |

### MEM @ CHA
Out: Grayson Allen (CHA), Kon Knueppel (CHA), Dennis Schroder (CHA), Grant Williams (CHA), Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM)

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 31.1<br><sub>33,27,33,25,30</sub> | 16.3<br><sub>23,18,20,19,23</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>12,8,3,4,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>4,6,5,4,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>4,2,4,5,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.5 | 1.7 | 26.5 |
| Ty Jerome | 98% | 30.4<br><sub>-,-,-,-,27</sub> | 22.0<br><sub>-,-,-,-,18</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>-,-,-,-,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.3<br><sub>-,-,-,-,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>-,-,-,-,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.2 | 2.6 | 30.7 |
| Cam Spencer | 98% | 28.2<br><sub>34,32,29,27,30</sub> | 12.0<br><sub>17,12,26,9,9</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>1,6,1,2,5</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 6.5<br><sub>8,9,7,11,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,1,5,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.4 | 21.7 |
| Jaylen Wells | 99% | 27.9<br><sub>25,27,26,24,25</sub> | 11.5<br><sub>5,8,5,22,8</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,4,4,7,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>2,3,2,0,0</sub> |  | 1.8<br><sub>1,2,1,4,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.1 | 0.8 | 15.9 |
| Javon Small | 98% | 23.9<br><sub>30,29,21,25,-</sub> | 10.5<br><sub>19,12,2,14,-</sub> |  | 3.4<br><sub>2,5,4,7,-</sub> |  | 4.4<br><sub>5,12,5,7,-</sub> |  | 1.4<br><sub>3,0,0,2,-</sub> |  | 0.9 | 0.2 | 1.3 | 18.2 |
| Taylor Hendricks | 91% | 23.5<br><sub>29,19,21,20,27</sub> | 9.8<br><sub>22,9,18,11,5</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>5,3,6,1,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>4,0,2,1,2</sub> |  | 1.1<br><sub>0,1,1,0,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.0 | 0.6 | 1.0 | 15.7 |
| Zach Edey | 88% | 22.7<br><sub>-,21,21,-,23</sub> | 8.9<br><sub>-,23,11,-,8</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.2<br><sub>-,10,2,-,2</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>-,1,1,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.5 | 1.4 | 1.3 | 17.2 |
| Olivier-Maxence Prosper | 88% | 19.7<br><sub>20,16,16,24,23</sub> | 9.4<br><sub>11,12,5,16,7</sub> |  | 3.6<br><sub>4,0,2,5,6</sub> |  | 0.9<br><sub>0,1,0,1,0</sub> |  | 0.9<br><sub>2,1,0,1,0</sub> |  | 0.8 | 0.2 | 0.8 | 13.9 |
| Isaiah Stewart | 98% | 18.3<br><sub>15,-,-,18,21</sub> | 8.1<br><sub>11,-,-,8,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,-,-,4,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>3,-,-,1,1</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.3 | 1.0 | 0.8 | 12.3 |
| Jahmai Mashack | 76% | 15.9<br><sub>2,2,13,26,22</sub> | 4.0<br><sub>0,0,3,0,0</sub> |  | 1.9<br><sub>0,0,2,3,2</sub> |  | 1.8<br><sub>0,1,2,4,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.7 | 0.3 | 0.8 | 7.7 |
| Kris Murray | 91% | 12.9<br><sub>19,6,6,4,12</sub> | 2.8<br><sub>3,0,5,0,7</sub> |  | 1.8<br><sub>2,1,0,1,0</sub> |  | 0.8<br><sub>3,0,0,0,0</sub> |  | 0.3<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.2 | 0.4 | 5.3 |
| Quinten Post | 72% | 9.8<br><sub>-,9,6,10,-</sub> | 3.7<br><sub>-,5,3,5,-</sub> |  | 1.8<br><sub>-,3,2,1,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,1,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.8 |
| Karim Lopez | 52% | 7.3<br><sub>2,1,-,4,-</sub> | 2.4<br><sub>0,0,-,3,-</sub> |  | 1.3<br><sub>2,0,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>0,0,-,1,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.2 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 99% | 34.2<br><sub>32,34,27,42,39</sub> | 21.4<br><sub>25,16,17,23,12</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 8.9<br><sub>13,8,4,11,10</sub> | 7.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>4,3,3,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>4,1,3,4,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 1.1 | 2.9 | 33.4 |
| Brandon Miller | 92% | 32.3<br><sub>-,-,24,32,33</sub> | 22.8<br><sub>-,-,5,28,19</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>-,-,2,2,8</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,-,4,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.2<br><sub>-,-,1,5,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.7 | 2.8 | 31.4 |
| Sion James | 99% | 31.3<br><sub>33,32,35,30,32</sub> | 8.4<br><sub>11,3,3,3,9</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>4,8,8,6,1</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 3.6<br><sub>4,6,4,4,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>3,0,1,0,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.3 | 1.4 | 16.8 |
| Moussa Diabate | 98% | 30.8<br><sub>-,32,26,38,30</sub> | 10.1<br><sub>-,7,12,5,21</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 11.2<br><sub>-,13,12,16,15</sub> | 9.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>-,2,2,2,2</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 1.1 | 1.3 | 1.8 | 23.8 |
| Coby White | 98% | 25.2<br><sub>20,20,20,26,26</sub> | 17.6<br><sub>10,21,21,19,11</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,3,0,3,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>9,3,1,4,9</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.6 | 0.2 | 2.8 | 25.5 |
| Royce O'Neale | 99% | 23.9<br><sub>23,22,19,34,21</sub> | 7.5<br><sub>10,7,3,13,9</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,4,3,4,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,1,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>2,2,1,4,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 0.9 | 12.9 |
| Christian Anderson | 91% | 19.3<br><sub>16,18,18,14,21</sub> | 8.3<br><sub>9,13,16,5,4</sub> |  | 2.1<br><sub>1,0,3,1,1</sub> |  | 2.8<br><sub>1,2,2,4,2</sub> |  | 1.1<br><sub>3,3,4,1,0</sub> |  | 0.6 | 0.3 | 1.4 | 13.2 |
| Ryan Kalkbrenner | 99% | 19.0<br><sub>35,16,18,14,17</sub> | 6.0<br><sub>8,2,5,6,6</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>15,6,5,3,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>3,1,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.5 | 1.0 | 12.6 |
| Tidjane Salaun | 97% | 14.6<br><sub>18,16,5,5,13</sub> | 5.5<br><sub>14,2,0,0,4</sub> |  | 3.4<br><sub>3,4,2,1,2</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 9.6 |
| Liam McNeeley | 58% | 13.0<br><sub>16,-,2,-,7</sub> | 5.1<br><sub>8,-,0,-,2</sub> |  | 2.4<br><sub>1,-,0,-,1</sub> |  | 1.0<br><sub>1,-,0,-,0</sub> |  | 0.6<br><sub>2,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 8.5 |
| Hannes Steinbach | 52% | 11.1<br><sub>13,-,-,-,-</sub> | 3.0<br><sub>2,-,-,-,-</sub> |  | 3.1<br><sub>3,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.6 | 6.6 |
| PJ Hall | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.6 | 0.7 | 6.8 |

</details>


### POR @ PHI
Out: Ariel Hukporti (PHI), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 67% | 34.5<br><sub>35,30,-,-,36</sub> | 25.8<br><sub>34,27,-,-,20</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>6,8,-,-,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>4,4,-,-,5</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>3,3,-,-,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.6 | 3.4 | 38.8 |
| Toumani Camara | 99% | 33.4<br><sub>36,26,33,37,35</sub> | 12.9<br><sub>14,3,10,18,6</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>2,0,8,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,0,1,4,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,0,2,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.6 | 1.2 | 19.4 |
| Damian Lillard | 99% | 32.6<br><sub>33,24,31,35,33</sub> | 22.0<br><sub>29,9,25,33,15</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>2,2,3,6,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,4,5,0,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>6,2,5,5,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.2 | 2.4 | 30.5 |
| Jrue Holiday | 99% | 29.9<br><sub>27,25,31,31,31</sub> | 14.8<br><sub>6,10,23,22,13</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>5,4,5,2,9</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.9<br><sub>5,3,6,7,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>0,2,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.3 | 2.2 | 24.1 |
| Donovan Clingan | 99% | 28.8<br><sub>27,22,32,26,31</sub> | 12.3<br><sub>13,10,12,7,22</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 11.8<br><sub>11,10,12,13,13</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,1,5,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>1,0,0,0,3</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.6 | 2.1 | 1.3 | 26.6 |
| Sidy Cissoko | 98% | 25.5<br><sub>26,28,32,31,23</sub> | 8.1<br><sub>3,5,6,13,11</sub> | 5.5 · –<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>4,4,5,5,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>1,3,1,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,1,2,1,3</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.4 | 1.0 | 13.3 |
| Scoot Henderson | 99% | 24.7<br><sub>23,23,21,35,23</sub> | 11.8<br><sub>11,10,9,27,3</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>0,1,1,7,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.2<br><sub>1,0,1,3,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>2,0,0,5,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 2.0 | 16.5 |
| Robert Williams III | 98% | 16.8<br><sub>17,15,16,-,17</sub> | 5.8<br><sub>2,2,6,-,4</sub> |  | 6.2<br><sub>7,5,8,-,3</sub> |  | 1.2<br><sub>1,2,4,-,0</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.5 | 1.1 | 0.7 | 13.2 |
| Jayson Kent | 86% | 11.5<br><sub>11,11,27,17,3</sub> | 3.9<br><sub>3,8,8,2,0</sub> |  | 1.4<br><sub>1,0,3,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.3<br><sub>1,2,2,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.8 |
| Branden Carlson | 88% | 9.7<br><sub>8,14,14,10,9</sub> | 2.8<br><sub>5,5,6,0,2</sub> |  | 2.1<br><sub>3,6,1,1,1</sub> |  | 0.4<br><sub>0,1,0,0,0</sub> |  | 0.1<br><sub>1,1,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 5.4 |
| Yang Hansen | 52% | 7.9<br><sub>-,7,-,12,-</sub> | 2.8<br><sub>-,0,-,2,-</sub> |  | 2.0<br><sub>-,1,-,1,-</sub> |  | 0.5<br><sub>-,3,-,1,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.2 | 0.6 | 5.3 |
| Micah Potter | 52% | 7.6<br><sub>-,7,1,-,-</sub> | 3.2<br><sub>-,2,0,-,-</sub> |  | 2.1<br><sub>-,4,0,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 5.7 |
| John Tonje | 48% | 7.3<br><sub>-,7,-,6,-</sub> | 2.8<br><sub>-,7,-,0,-</sub> |  | 1.8<br><sub>-,4,-,3,-</sub> |  | 0.6<br><sub>-,3,-,0,-</sub> |  | 0.2<br><sub>-,1,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.2 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 84% | 33.8<br><sub>35,36,35,-,36</sub> | 21.7<br><sub>27,27,24,-,17</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>2,4,1,-,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>8,6,9,-,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>1,5,4,-,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.5 | 2.2 | 30.1 |
| VJ Edgecombe | 97% | 32.3<br><sub>36,31,33,43,38</sub> | 12.3<br><sub>15,11,14,24,16</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>8,4,9,8,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>8,6,4,6,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>1,0,1,4,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.6 | 0.5 | 1.5 | 21.5 |
| Jaylen Brown | 92% | 32.1<br><sub>36,32,33,-,-</sub> | 21.0<br><sub>18,31,31,-,-</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>6,2,13,-,-</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>2,2,4,-,-</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,3,3,-,-</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.5 | 3.0 | 30.5 |
| LeBron James | 98% | 31.0<br><sub>-,33,-,31,35</sub> | 16.0<br><sub>-,15,-,22,21</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>-,7,-,3,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>-,11,-,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>-,0,-,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.6 | 2.5 | 28.3 |
| Joel Embiid | 98% | 30.5<br><sub>28,-,32,36,34</sub> | 22.4<br><sub>20,-,37,26,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>4,-,5,6,17</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 4.0<br><sub>3,-,1,7,9</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>0,-,2,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 1.1 | 2.8 | 34.2 |
| Kentavious Caldwell-Pope | 99% | 21.4<br><sub>27,22,31,32,35</sub> | 4.9<br><sub>11,9,0,8,11</sub> |  | 2.4<br><sub>4,5,2,8,1</sub> |  | 1.5<br><sub>5,0,3,1,2</sub> |  | 0.7<br><sub>3,2,0,2,3</sub> |  | 0.9 | 0.3 | 0.7 | 8.8 |
| Anfernee Simons | 98% | 20.8<br><sub>23,15,26,38,26</sub> | 9.1<br><sub>17,12,9,18,18</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>3,0,1,2,0</sub> |  | 1.4<br><sub>2,0,2,2,1</sub> |  | 1.5<br><sub>5,1,1,3,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.1 | 0.9 | 12.3 |
| Dean Wade | 70% | 20.6<br><sub>34,35,32,-,-</sub> | 4.1<br><sub>6,12,8,-,-</sub> |  | 3.7<br><sub>5,7,11,-,-</sub> |  | 1.2<br><sub>2,3,1,-,-</sub> |  | 0.5<br><sub>2,3,1,-,-</sub> |  | 0.8 | 0.3 | 0.5 | 8.9 |
| Jabari Walker | 91% | 12.8<br><sub>16,25,16,13,20</sub> | 5.6<br><sub>9,11,12,6,9</sub> |  | 3.7<br><sub>8,7,5,5,7</sub> |  | 0.8<br><sub>1,1,1,2,4</sub> |  | 0.5<br><sub>1,3,1,1,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.2 |
| Dominick Barlow | 91% | 10.2<br><sub>-,-,-,-,11</sub> | 3.5<br><sub>-,-,-,-,12</sub> |  | 2.1<br><sub>-,-,-,-,4</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.4 | 0.4 | 6.2 |
| Adem Bona | 91% | 7.2<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.4 | 4.3 |
| Rayan Rupert | 36% | 6.7<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.3 |
| Justin Edwards | 52% | 6.5<br><sub>1,-,-,13,-</sub> | 2.7<br><sub>0,-,-,2,-</sub> |  | 0.9<br><sub>1,-,-,1,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Labaron Philon Jr. | 71% | 6.2<br><sub>2,6,-,17,6</sub> | 2.8<br><sub>0,3,-,10,2</sub> |  | 0.8<br><sub>0,1,-,1,0</sub> |  | 0.7<br><sub>0,0,-,2,0</sub> |  | 0.2<br><sub>0,1,-,2,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Tacko Fall | 58% | 5.8<br><sub>1,5,-,10,-</sub> | 4.8<br><sub>0,0,-,2,-</sub> |  | 1.7<br><sub>0,3,-,3,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 6.9 |
| Caleb Love | 48% | 5.2<br><sub>1,-,-,6,-</sub> | 2.1<br><sub>0,-,-,3,-</sub> |  | 0.8<br><sub>0,-,-,1,-</sub> |  | 0.6<br><sub>0,-,-,1,-</sub> |  | 0.2<br><sub>0,-,-,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.5 |

</details>


### OKC @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND), Alex Caruso (OKC), Shai Gilgeous-Alexander (OKC), Chet Holmgren (OKC), Aday Mara (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jared McCain | 99% | 33.7<br><sub>31,31,30,33,30</sub> | 22.6<br><sub>10,23,12,18,18</sub> |  | 4.3<br><sub>6,4,1,3,3</sub> |  | 2.5<br><sub>3,2,1,1,0</sub> |  | 3.2<br><sub>2,7,1,4,3</sub> |  | 1.0 | 0.2 | 1.9 | 29.4 |
| Ajay Mitchell | 98% | 32.4<br><sub>-,-,27,34,31</sub> | 23.6<br><sub>-,-,14,13,8</sub> |  | 4.4<br><sub>-,-,3,6,2</sub> |  | 5.4<br><sub>-,-,5,6,4</sub> |  | 1.3<br><sub>-,-,1,0,1</sub> |  | 1.4 | 0.4 | 2.0 | 33.3 |
| Bennett Stirtz | 98% | 30.4<br><sub>25,12,17,17,25</sub> | 14.4<br><sub>6,5,0,6,18</sub> |  | 2.5<br><sub>1,1,1,0,2</sub> |  | 2.5<br><sub>1,0,2,2,2</sub> |  | 2.3<br><sub>2,1,0,2,4</sub> |  | 1.1 | 0.2 | 1.1 | 19.4 |
| Kenrich Williams | 98% | 29.8<br><sub>26,35,19,23,28</sub> | 14.6<br><sub>11,8,10,10,6</sub> |  | 5.9<br><sub>2,8,1,5,2</sub> |  | 2.8<br><sub>2,4,2,1,4</sub> |  | 1.7<br><sub>2,0,2,0,1</sub> |  | 1.1 | 0.3 | 1.1 | 23.3 |
| Isaiah Hartenstein | 99% | 27.5<br><sub>34,30,18,27,28</sub> | 12.1<br><sub>20,21,3,6,5</sub> |  | 12.1<br><sub>11,16,11,17,8</sub> |  | 5.1<br><sub>6,6,2,6,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.7 | 2.1 | 29.2 |
| Nique Clifford | 97% | 26.5<br><sub>16,12,24,13,15</sub> | 11.0<br><sub>5,0,9,7,4</sub> |  | 4.2<br><sub>3,0,3,0,5</sub> |  | 2.5<br><sub>1,0,0,0,1</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 1.0 | 0.3 | 1.4 | 17.7 |
| Micah Peavy | 91% | 24.5<br><sub>12,-,13,-,9</sub> | 8.4<br><sub>0,-,5,-,2</sub> |  | 4.5<br><sub>3,-,3,-,2</sub> |  | 1.1<br><sub>0,-,1,-,0</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.8 | 0.3 | 0.4 | 14.0 |
| Josh Dix | 58% | 22.9<br><sub>-,17,-,-,-</sub> | 8.4<br><sub>-,0,-,-,-</sub> |  | 3.0<br><sub>-,4,-,-,-</sub> |  | 1.6<br><sub>-,3,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.8 | 0.3 | 0.5 | 12.9 |
| Brooks Barnhizer | 48% | 14.9<br><sub>-,-,4,-,-</sub> | 4.2<br><sub>-,-,0,-,-</sub> |  | 3.3<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.6 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 93% | 34.0<br><sub>32,32,34,33,30</sub> | 22.3<br><sub>28,19,31,24,21</sub> |  | 6.7<br><sub>8,3,2,4,7</sub> |  | 4.3<br><sub>5,2,2,3,2</sub> |  | 1.8<br><sub>2,2,0,2,2</sub> |  | 0.9 | 0.3 | 2.4 | 33.2 |
| Andrew Nembhard | 91% | 33.4<br><sub>34,34,-,-,26</sub> | 16.8<br><sub>17,12,-,-,12</sub> |  | 3.0<br><sub>2,4,-,-,3</sub> |  | 8.5<br><sub>10,6,-,-,8</sub> |  | 2.1<br><sub>3,1,-,-,3</sub> |  | 0.8 | 0.2 | 2.6 | 28.2 |
| Aaron Nesmith | 93% | 29.8<br><sub>22,33,36,29,29</sub> | 13.1<br><sub>2,18,12,2,2</sub> |  | 4.0<br><sub>1,7,4,3,10</sub> |  | 2.2<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> |  | 0.7 | 0.5 | 1.4 | 19.3 |
| Ivica Zubac | 88% | 26.3<br><sub>31,26,22,24,27</sub> | 11.6<br><sub>20,12,8,4,21</sub> |  | 9.0<br><sub>12,13,5,3,10</sub> |  | 1.9<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.6 | 22.6 |
| Kelly Oubre Jr. | 91% | 25.4<br><sub>34,30,29,23,23</sub> | 11.7<br><sub>14,16,16,17,17</sub> |  | 4.0<br><sub>6,5,4,4,6</sub> |  | 1.3<br><sub>1,0,2,0,0</sub> |  | 1.4<br><sub>0,1,2,2,3</sub> |  | 0.8 | 0.6 | 1.2 | 17.1 |
| Quenton Jackson | 98% | 21.3<br><sub>21,20,30,22,18</sub> | 9.6<br><sub>4,3,15,15,3</sub> |  | 3.1<br><sub>2,5,6,2,2</sub> |  | 3.2<br><sub>2,4,8,3,2</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> |  | 0.9 | 0.2 | 1.4 | 16.0 |
| Obi Toppin | 88% | 19.9<br><sub>16,16,14,17,26</sub> | 11.6<br><sub>8,9,5,6,17</sub> |  | 4.2<br><sub>3,3,2,1,3</sub> |  | 1.9<br><sub>1,1,1,1,2</sub> |  | 1.6<br><sub>2,1,0,0,2</sub> |  | 0.5 | 0.2 | 1.0 | 17.7 |
| Jarace Walker | 88% | 15.9<br><sub>7,-,14,17,11</sub> | 6.7<br><sub>1,-,2,1,8</sub> |  | 3.6<br><sub>1,-,5,3,1</sub> |  | 1.6<br><sub>0,-,2,1,3</sub> |  | 0.9<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.3 | 1.0 | 11.9 |
| Jalen Slawson | 91% | 13.3<br><sub>12,10,14,12,14</sub> | 4.4<br><sub>2,1,8,5,4</sub> |  | 2.9<br><sub>3,4,5,4,2</sub> |  | 1.3<br><sub>1,0,2,2,2</sub> |  | 0.4<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 0.7 | 8.7 |
| Braden Smith | 67% | 13.2<br><sub>-,-,-,18,11</sub> | 4.5<br><sub>-,-,-,8,5</sub> |  | 1.6<br><sub>-,-,-,5,3</sub> |  | 2.6<br><sub>-,-,-,3,5</sub> |  | 0.3<br><sub>-,-,-,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 8.7 |
| Jay Huff | 91% | 11.7<br><sub>11,8,18,15,1</sub> | 5.3<br><sub>6,8,11,5,0</sub> |  | 2.2<br><sub>4,1,0,3,0</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.6<br><sub>0,2,3,0,0</sub> |  | 0.2 | 0.7 | 0.5 | 8.4 |
| Larry Nance Jr. | 97% | 11.4<br><sub>5,14,7,9,11</sub> | 4.0<br><sub>5,2,4,3,7</sub> |  | 2.3<br><sub>0,2,2,1,2</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.5<br><sub>1,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 7.0 |
| Kobe Brown | 86% | 9.4<br><sub>-,-,3,2,-</sub> | 3.5<br><sub>-,-,0,0,-</sub> |  | 1.8<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 6.0 |

</details>


### MIL @ TOR
Out: RJ Barrett (TOR), Kawhi Leonard (TOR), Kam Jones (MIL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.2–116.2 | MIL 26% | 3.86 / 1.35 | TOR -8.5 | 223.5 | TOR -10.5 covers 46%; o223.5 50% |
| Expected (weighted by chance each plays) | 107.3–116.3 | MIL 26% | 3.83 / 1.35 | TOR -8.5 | 223.5 | TOR -10.5 covers 46%; o223.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ousmane Dieng (MIL) | Questionable | 55% | 7.7 | 2.9 | 1.2 | 0.8 | 0.2 | 0.2 | 0.1 | 0.5 | 4.9 | small |

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 99% | 30.0<br><sub>34,20,24,31,40</sub> | 18.2<br><sub>18,5,8,19,50</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>1,5,2,4,11</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.0<br><sub>2,3,4,3,7</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>2,0,0,4,7</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 2.5 | 26.4 |
| Kyle Kuzma | 99% | 25.9<br><sub>31,22,30,-,33</sub> | 11.9<br><sub>14,14,26,-,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>4,6,5,-,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,2,1,-,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3<br><sub>1,3,2,-,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.3 | 1.9 | 18.4 |
| Jaime Jaquez Jr. | 99% | 24.2<br><sub>28,30,23,22,25</sub> | 12.1<br><sub>22,6,10,9,9</sub> |  | 3.8<br><sub>6,5,2,1,0</sub> |  | 2.8<br><sub>4,4,5,2,1</sub> |  | 1.2<br><sub>5,2,1,1,1</sub> |  | 0.6 | 0.2 | 1.9 | 18.8 |
| Myles Turner | 99% | 23.6<br><sub>31,23,21,-,26</sub> | 8.2<br><sub>14,8,4,-,5</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>11,7,5,-,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>3,1,4,-,5</sub> |  | 1.1<br><sub>4,1,0,-,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.6 | 1.5 | 1.2 | 14.9 |
| Ryan Rollins | 99% | 23.2<br><sub>29,-,-,21,28</sub> | 11.0<br><sub>8,-,-,15,8</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>10,-,-,3,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>2,-,-,6,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,-,-,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 2.2 | 18.4 |
| Brayden Burries | 98% | 22.3<br><sub>19,29,25,28,26</sub> | 10.2<br><sub>3,13,20,14,26</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>4,8,7,3,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,4,1,3,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>1,2,3,2,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 1.4 | 17.3 |
| Kel'el Ware | 98% | 17.3<br><sub>17,25,17,26,22</sub> | 7.5<br><sub>10,8,11,11,6</sub> |  | 5.5<br><sub>6,11,3,5,8</sub> |  | 0.8<br><sub>1,2,1,0,3</sub> |  | 0.6<br><sub>2,1,1,2,0</sub> |  | 0.5 | 0.8 | 1.3 | 13.8 |
| Nate Ament | 97% | 15.7<br><sub>22,17,17,35,14</sub> | 6.0<br><sub>9,5,7,18,2</sub> |  | 2.5<br><sub>3,2,4,9,1</sub> |  | 0.6<br><sub>1,1,1,0,0</sub> |  | 0.6<br><sub>2,1,0,2,0</sub> |  | 0.5 | 0.2 | 0.8 | 9.1 |
| Kasparas Jakucionis | 88% | 14.4<br><sub>-,26,26,22,10</sub> | 6.6<br><sub>-,25,20,18,2</sub> |  | 1.9<br><sub>-,5,3,3,3</sub> |  | 2.4<br><sub>-,5,5,2,3</sub> |  | 0.7<br><sub>-,4,3,3,0</sub> |  | 0.5 | 0.1 | 1.2 | 10.9 |
| Cormac Ryan | 52% | 14.0<br><sub>-,-,-,-,-</sub> | 7.1<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 9.6 |
| Pete Nance | 96% | 13.5<br><sub>-,-,-,28,-</sub> | 4.1<br><sub>-,-,-,7,-</sub> |  | 2.0<br><sub>-,-,-,3,-</sub> |  | 0.9<br><sub>-,-,-,3,-</sub> |  | 0.4<br><sub>-,-,-,1,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.0 |
| AJ Green | 84% | 12.3<br><sub>8,6,14,-,12</sub> | 4.3<br><sub>0,0,11,-,9</sub> |  | 1.2<br><sub>0,0,0,-,0</sub> |  | 0.8<br><sub>2,0,1,-,0</sub> |  | 0.7<br><sub>0,0,3,-,3</sub> |  | 0.2 | 0.1 | 0.5 | 6.3 |
| Gary Trent Jr. | 64% | 9.2<br><sub>16,30,16,7,-</sub> | 4.1<br><sub>1,18,1,0,-</sub> |  | 0.7<br><sub>0,2,1,1,-</sub> |  | 0.4<br><sub>0,1,0,0,-</sub> |  | 0.5<br><sub>0,4,0,0,-</sub> |  | 0.3 | 0.0 | 0.4 | 5.2 |
| Caris LeVert | 52% | 8.4<br><sub>-,-,8,11,5</sub> | 3.4<br><sub>-,-,8,3,0</sub> |  | 1.1<br><sub>-,-,3,3,1</sub> |  | 0.9<br><sub>-,-,2,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.5 |
| Jericho Sims | 64% | 8.4<br><sub>-,11,18,10,-</sub> | 2.0<br><sub>-,4,4,0,-</sub> |  | 2.1<br><sub>-,2,6,0,-</sub> |  | 0.6<br><sub>-,0,2,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.7 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 35.5<br><sub>-,36,34,-,37</sub> | 26.2<br><sub>-,30,20,-,29</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>-,9,4,-,5</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>-,4,2,-,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>-,4,1,-,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.6 | 1.2 | 3.1 | 40.9 |
| Ja'Kobe Walter | 99% | 32.7<br><sub>32,36,33,38,33</sub> | 13.8<br><sub>6,7,25,18,8</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>5,2,1,7,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>0,1,2,6,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.6<br><sub>1,1,7,3,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.3 | 1.0 | 20.2 |
| Immanuel Quickley | 91% | 32.5<br><sub>28,38,34,34,33</sub> | 19.6<br><sub>26,17,14,24,18</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>4,6,1,3,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.6<br><sub>6,6,7,5,10</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 3.0<br><sub>3,3,2,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.1 | 1.7 | 30.1 |
| Jakob Poeltl | 96% | 27.2<br><sub>25,17,18,29,32</sub> | 11.7<br><sub>9,11,3,8,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>5,5,6,9,9</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>3,1,1,5,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.0 | 1.4 | 22.6 |
| Allen Graves | 98% | 24.3<br><sub>13,16,13,31,33</sub> | 8.5<br><sub>0,2,3,9,20</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>2,5,2,4,10</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>0,3,1,0,1</sub> |  | 1.1<br><sub>0,0,1,1,2</sub> |  | 0.8 | 0.6 | 0.8 | 14.6 |
| Collin Murray-Boyles | 70% | 24.2<br><sub>32,40,33,5,-</sub> | 11.1<br><sub>14,6,8,1,-</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>0,13,1,2,-</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>4,2,3,1,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.4<br><sub>1,0,0,0,-</sub> | 0.5<br><sub>o 43% · u 57%</sub> | 1.1 | 1.2 | 1.4 | 18.9 |
| Jamal Shead | 99% | 23.1<br><sub>22,26,20,24,15</sub> | 8.3<br><sub>5,19,7,15,0</sub> |  | 1.9<br><sub>1,2,0,1,1</sub> |  | 6.3<br><sub>5,4,6,6,4</sub> |  | 1.1<br><sub>1,3,1,1,0</sub> |  | 1.0 | 0.2 | 1.6 | 16.5 |
| Jamison Battle | 98% | 21.5<br><sub>25,8,7,33,20</sub> | 10.3<br><sub>13,0,0,19,10</sub> |  | 2.9<br><sub>1,3,1,5,5</sub> |  | 0.9<br><sub>1,0,0,0,0</sub> |  | 1.9<br><sub>3,0,0,5,2</sub> |  | 0.5 | 0.1 | 0.6 | 14.1 |
| Trayce Jackson-Davis | 63% | 14.8<br><sub>-,-,-,17,16</sub> | 6.0<br><sub>-,-,-,3,8</sub> |  | 4.8<br><sub>-,-,-,7,2</sub> |  | 1.1<br><sub>-,-,-,1,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.8 | 0.9 | 0.7 | 11.9 |
| Alijah Martin | 96% | 14.7<br><sub>18,12,8,17,16</sub> | 5.6<br><sub>7,2,0,2,0</sub> |  | 2.2<br><sub>4,3,2,2,2</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.6 | 0.2 | 0.8 | 8.9 |
| Kyle Anderson | 52% | 9.1<br><sub>5,-,-,4,-</sub> | 2.8<br><sub>0,-,-,0,-</sub> |  | 1.7<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.3 | 0.5 | 6.1 |
| Malachi Smith | 96% | 8.1<br><sub>2,-,-,8,5</sub> | 2.8<br><sub>0,-,-,0,2</sub> |  | 1.3<br><sub>0,-,-,1,0</sub> |  | 1.1<br><sub>0,-,-,3,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.1 |
| Kevin McCullar Jr. | 16% | 7.3<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.6 |
| Jaden Bradley | 48% | 6.9<br><sub>2,-,-,-,-</sub> | 2.4<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |

</details>


### BKN @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Chaney Johnson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Nolan Traore (BKN)

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 99% | 34.2<br><sub>29,31,34,27,39</sub> | 20.5<br><sub>17,22,33,17,27</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>4,4,6,0,9</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>5,5,1,4,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>0,3,2,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 3.5 | 31.3 |
| Michael Porter Jr. | 88% | 33.9<br><sub>28,-,40,27,34</sub> | 19.5<br><sub>22,-,25,5,16</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>6,-,6,3,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>3,-,2,1,5</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.6<br><sub>4,-,2,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.4 | 2.4 | 28.3 |
| Egor Demin | 98% | 25.6<br><sub>23,27,26,31,21</sub> | 10.8<br><sub>22,11,9,22,6</sub> |  | 3.0<br><sub>1,1,3,4,3</sub> |  | 3.0<br><sub>1,2,4,4,2</sub> |  | 1.7<br><sub>4,3,2,3,0</sub> |  | 0.8 | 0.3 | 1.8 | 16.8 |
| Day'Ron Sharpe | 99% | 25.3<br><sub>19,28,25,22,26</sub> | 10.2<br><sub>15,16,6,6,17</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 8.1<br><sub>4,11,9,5,11</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>5,5,5,1,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 0.3<br><sub>2,0,0,0,0</sub> |  | 1.1 | 1.2 | 2.0 | 22.1 |
| Mikel Brown Jr. | 98% | 24.7<br><sub>-,20,18,27,24</sub> | 12.1<br><sub>-,6,3,15,18</sub> |  | 2.1<br><sub>-,1,1,1,1</sub> |  | 3.4<br><sub>-,2,5,4,0</sub> |  | 1.7<br><sub>-,2,1,2,3</sub> |  | 0.8 | 0.2 | 2.2 | 17.6 |
| Noah Clowney | 99% | 23.5<br><sub>19,35,24,19,22</sub> | 8.2<br><sub>16,15,9,7,0</sub> |  | 4.0<br><sub>3,7,3,3,2</sub> |  | 1.2<br><sub>0,3,3,1,2</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 0.7 | 0.7 | 1.1 | 13.4 |
| Danny Wolf | 88% | 22.8<br><sub>29,28,11,23,26</sub> | 8.9<br><sub>10,14,3,6,20</sub> |  | 5.2<br><sub>11,6,2,6,5</sub> |  | 2.0<br><sub>4,1,1,2,2</sub> |  | 1.0<br><sub>1,4,1,1,4</sub> |  | 0.6 | 0.6 | 1.5 | 16.2 |
| Moritz Wagner | 98% | 18.5<br><sub>19,18,10,20,22</sub> | 9.1<br><sub>16,10,4,11,3</sub> |  | 4.2<br><sub>3,6,5,2,5</sub> |  | 1.5<br><sub>4,4,1,3,2</sub> |  | 0.7<br><sub>2,2,0,2,1</sub> |  | 0.7 | 0.3 | 1.2 | 14.8 |
| Keon Ellis | 91% | 17.1<br><sub>26,7,20,6,8</sub> | 3.9<br><sub>11,0,8,3,0</sub> |  | 1.8<br><sub>4,0,2,1,1</sub> |  | 1.1<br><sub>3,1,0,0,1</sub> |  | 0.5<br><sub>2,0,2,1,0</sub> |  | 1.0 | 0.6 | 0.5 | 6.8 |
| Terance Mann | 58% | 14.4<br><sub>18,9,-,5,-</sub> | 3.4<br><sub>6,2,-,0,-</sub> |  | 1.8<br><sub>1,1,-,1,-</sub> |  | 1.4<br><sub>3,1,-,0,-</sub> |  | 0.3<br><sub>2,0,-,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 6.5 |
| Josh Minott | 52% | 9.5<br><sub>7,2,-,4,-</sub> | 4.4<br><sub>0,0,-,0,-</sub> |  | 1.6<br><sub>2,0,-,0,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.3 | 0.5 | 6.5 |
| Grant Nelson | 62% | 9.1 | 3.3 |  | 1.8 |  | 0.7 |  | 0.0 |  | 0.3 | 0.9 | 0.5 | 5.8 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 34.5<br><sub>37,31,37,39,36</sub> | 17.8<br><sub>18,13,22,17,25</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>5,6,5,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.4<br><sub>6,3,4,1,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>2,0,2,4,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 1.0 | 2.0 | 26.6 |
| Ayo Dosunmu | 99% | 32.8<br><sub>33,30,39,32,34</sub> | 17.8<br><sub>24,8,30,6,19</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>5,5,4,4,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>0,2,5,4,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>0,2,7,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.4 | 2.3 | 26.1 |
| Jonathan Kuminga | 88% | 31.4<br><sub>35,29,-,35,37</sub> | 14.7<br><sub>11,13,-,23,16</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,9,-,3,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>3,1,-,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,-,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.7 | 1.9 | 23.0 |
| LaMelo Ball | 99% | 30.2<br><sub>30,24,31,35,32</sub> | 20.5<br><sub>19,6,18,15,12</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>8,5,9,8,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 6.4<br><sub>6,0,2,8,7</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.6<br><sub>4,2,3,3,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6 | 0.3 | 3.1 | 31.6 |
| Rudy Gobert | 99% | 30.0<br><sub>27,32,22,35,32</sub> | 9.5<br><sub>1,18,0,9,7</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 10.8<br><sub>10,15,4,7,11</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>4,3,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.4 | 22.0 |
| Terrence Shannon Jr. | 98% | 24.0<br><sub>22,35,24,21,26</sub> | 13.6<br><sub>14,34,12,10,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>6,3,1,4,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>0,6,4,3,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>0,3,1,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.1 | 1.4 | 19.4 |
| Trey Lyles | 99% | 18.4<br><sub>19,19,31,16,12</sub> | 5.9<br><sub>5,9,8,8,3</sub> |  | 3.9<br><sub>1,3,7,6,3</sub> |  | 1.1<br><sub>2,1,4,1,1</sub> |  | 0.8<br><sub>0,2,2,2,1</sub> |  | 0.5 | 0.3 | 0.6 | 10.9 |
| Joan Beringer | 98% | 17.0<br><sub>13,16,26,13,16</sub> | 6.2<br><sub>2,0,3,5,0</sub> |  | 5.9<br><sub>5,4,13,3,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 0.8 | 12.6 |
| Bones Hyland | 98% | 16.3<br><sub>21,13,17,15,16</sub> | 9.7<br><sub>12,5,13,6,7</sub> |  | 1.7<br><sub>1,1,2,1,0</sub> |  | 2.9<br><sub>2,5,1,1,4</sub> |  | 1.4<br><sub>3,0,3,1,1</sub> |  | 0.8 | 0.2 | 1.1 | 14.3 |
| Cody Williams | 52% | 7.8<br><sub>-,4,13,-,-</sub> | 0.2<br><sub>-,0,0,-,-</sub> |  | 1.2<br><sub>-,1,1,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 1.7 |
| Zyon Pullin | 38% | 6.5<br><sub>-,4,-,-,-</sub> | 2.6<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Isaiah Evans | 38% | 5.9<br><sub>-,4,-,-,-</sub> | 4.7<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 6.0 |
| Johni Broome | 38% | 5.5<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### CLE @ CHI
Out: Nic Claxton (CHI), Norman Powell (CHI), Caleb Wilson (CHI), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE)

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 99% | 32.4<br><sub>35,-,34,36,40</sub> | 19.8<br><sub>20,-,9,14,51</sub> |  | 4.7<br><sub>6,-,4,6,6</sub> |  | 6.6<br><sub>8,-,10,9,6</sub> |  | 2.7<br><sub>2,-,2,3,7</sub> |  | 1.4 | 0.5 | 2.8 | 31.1 |
| Donovan Mitchell | 99% | 31.2<br><sub>33,-,36,35,29</sub> | 25.3<br><sub>25,-,39,34,20</sub> |  | 4.5<br><sub>4,-,4,4,3</sub> |  | 4.9<br><sub>7,-,4,3,3</sub> |  | 2.8<br><sub>5,-,2,2,2</sub> |  | 1.5 | 0.3 | 2.5 | 34.7 |
| Jarrett Allen | 88% | 26.0<br><sub>32,-,30,30,31</sub> | 14.0<br><sub>9,-,13,19,6</sub> |  | 8.7<br><sub>8,-,14,9,8</sub> |  | 1.6<br><sub>1,-,3,4,4</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.9 | 1.2 | 1.2 | 24.3 |
| Peyton Watson | 88% | 25.3<br><sub>30,-,22,-,29</sub> | 12.1<br><sub>4,-,14,-,15</sub> |  | 4.3<br><sub>4,-,4,-,4</sub> |  | 2.2<br><sub>2,-,0,-,3</sub> |  | 1.2<br><sub>0,-,2,-,3</sub> |  | 0.9 | 1.2 | 1.5 | 18.7 |
| Meleek Thomas | 96% | 21.0<br><sub>18,34,30,22,20</sub> | 11.0<br><sub>12,20,10,14,4</sub> |  | 2.6<br><sub>0,4,6,2,1</sub> |  | 1.9<br><sub>3,2,3,2,4</sub> |  | 1.6<br><sub>2,3,1,4,0</sub> |  | 1.1 | 0.2 | 1.0 | 15.4 |
| Tyrese Proctor | 97% | 20.7<br><sub>27,34,29,26,24</sub> | 10.0<br><sub>22,24,17,8,5</sub> |  | 3.1<br><sub>4,11,3,1,1</sub> |  | 2.8<br><sub>3,10,2,1,2</sub> |  | 1.4<br><sub>5,4,2,2,1</sub> |  | 0.9 | 0.1 | 0.9 | 15.8 |
| Sam Merrill | 98% | 19.9<br><sub>-,-,-,23,25</sub> | 8.2<br><sub>-,-,-,7,6</sub> |  | 2.2<br><sub>-,-,-,2,1</sub> |  | 1.8<br><sub>-,-,-,3,1</sub> |  | 1.4<br><sub>-,-,-,1,2</sub> |  | 0.8 | 0.1 | 0.5 | 12.2 |
| Mario Hezonja | 98% | 17.6<br><sub>9,34,15,28,20</sub> | 8.0<br><sub>4,22,9,16,10</sub> |  | 4.8<br><sub>4,7,4,7,10</sub> |  | 1.8<br><sub>0,4,2,5,3</sub> |  | 0.9<br><sub>0,2,1,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 14.5 |
| Jaylon Tyson | 91% | 16.3<br><sub>30,34,-,-,-</sub> | 7.3<br><sub>16,18,-,-,-</sub> |  | 2.9<br><sub>3,4,-,-,-</sub> |  | 1.6<br><sub>1,4,-,-,-</sub> |  | 0.9<br><sub>4,3,-,-,-</sub> |  | 0.6 | 0.2 | 0.8 | 11.9 |
| Thomas Bryant | 88% | 15.2<br><sub>16,27,18,12,16</sub> | 8.9<br><sub>9,19,9,5,9</sub> |  | 4.4<br><sub>1,11,5,4,6</sub> |  | 0.9<br><sub>1,3,4,0,0</sub> |  | 0.9<br><sub>0,2,0,1,2</sub> |  | 0.4 | 0.5 | 0.5 | 14.2 |
| Norchad Omier | 72% | 9.6<br><sub>-,27,13,16,6</sub> | 3.3<br><sub>-,13,4,2,2</sub> |  | 3.2<br><sub>-,8,6,7,1</sub> |  | 0.8<br><sub>-,2,2,0,0</sub> |  | 0.1<br><sub>-,1,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 7.3 |
| Craig Porter Jr. | 67% | 9.2<br><sub>9,28,14,12,-</sub> | 2.4<br><sub>0,9,2,2,-</sub> |  | 1.9<br><sub>2,9,1,3,-</sub> |  | 1.8<br><sub>2,6,3,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.3 | 0.5 | 6.0 |
| Riley Minix | 48% | 6.5<br><sub>-,22,-,-,-</sub> | 2.4<br><sub>-,2,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.7 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matas Buzelis | 99% | 30.7<br><sub>29,30,31,30,25</sub> | 18.3<br><sub>11,18,23,25,9</sub> |  | 5.7<br><sub>6,9,3,5,5</sub> |  | 2.2<br><sub>2,2,0,4,1</sub> |  | 2.5<br><sub>3,2,3,5,1</sub> |  | 0.7 | 1.0 | 2.4 | 26.1 |
| Isaac Okoro | 99% | 30.0<br><sub>41,31,32,25,29</sub> | 11.2<br><sub>15,9,13,12,9</sub> |  | 3.2<br><sub>3,7,6,3,7</sub> |  | 2.0<br><sub>2,4,2,4,1</sub> |  | 1.2<br><sub>2,0,3,4,1</sub> |  | 0.9 | 0.4 | 1.0 | 16.5 |
| Josh Giddey | 99% | 29.8<br><sub>39,26,24,28,23</sub> | 14.7<br><sub>15,8,4,18,2</sub> |  | 7.0<br><sub>10,8,4,14,6</sub> |  | 8.9<br><sub>14,5,8,9,7</sub> |  | 1.6<br><sub>3,2,1,1,0</sub> |  | 0.9 | 0.6 | 3.0 | 30.5 |
| Jalen Smith | 98% | 28.2<br><sub>32,-,28,21,-</sub> | 15.3<br><sub>15,-,17,14,-</sub> |  | 8.3<br><sub>12,-,11,6,-</sub> |  | 2.0<br><sub>3,-,3,3,-</sub> |  | 1.9<br><sub>1,-,3,2,-</sub> |  | 0.7 | 0.9 | 1.3 | 25.5 |
| Patrick Williams | 88% | 24.3<br><sub>24,26,13,13,23</sub> | 8.9<br><sub>13,14,0,2,6</sub> |  | 3.3<br><sub>4,5,0,1,3</sub> |  | 1.8<br><sub>2,1,0,2,1</sub> |  | 1.2<br><sub>4,2,0,0,0</sub> |  | 0.8 | 0.5 | 1.1 | 14.0 |
| Tre Jones | 99% | 24.3<br><sub>15,24,23,16,25</sub> | 14.2<br><sub>4,16,16,10,12</sub> |  | 2.9<br><sub>1,0,2,2,1</sub> |  | 5.0<br><sub>3,4,6,6,7</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 1.1 | 0.2 | 1.5 | 22.0 |
| Buddy Hield | 88% | 21.3<br><sub>25,20,19,19,23</sub> | 10.7<br><sub>12,16,6,11,15</sub> |  | 2.9<br><sub>3,4,4,1,4</sub> |  | 1.9<br><sub>3,2,2,2,0</sub> |  | 1.8<br><sub>2,4,2,3,4</sub> |  | 0.8 | 0.3 | 1.1 | 15.4 |
| Zach Collins | 71% | 17.0<br><sub>-,28,-,11,15</sub> | 7.0<br><sub>-,8,-,3,6</sub> |  | 4.5<br><sub>-,5,-,2,2</sub> |  | 1.8<br><sub>-,4,-,0,4</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.5 | 0.5 | 0.9 | 13.3 |
| Noa Essengue | 98% | 15.3<br><sub>8,7,14,15,15</sub> | 6.0<br><sub>5,0,1,5,8</sub> |  | 3.2<br><sub>1,1,2,3,4</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.6<br><sub>1,0,0,0,2</sub> |  | 0.5 | 0.2 | 0.8 | 9.9 |
| Leonard Miller | 64% | 14.8<br><sub>-,17,1,7,-</sub> | 6.8<br><sub>-,4,0,4,-</sub> |  | 3.4<br><sub>-,3,0,2,-</sub> |  | 0.9<br><sub>-,4,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 11.1 |
| Orlando Robinson | 30% | 12.9<br><sub>-,-,-,-,-</sub> | 5.2<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.7 | 10.1 |
| Jordan Hawkins | 52% | 12.8<br><sub>-,-,4,-,-</sub> | 5.7<br><sub>-,-,0,-,-</sub> |  | 1.6<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 8.1 |
| Tobe Awaka | 58% | 9.8<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 3.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.4 | 0.5 | 7.4 |
| Jaylin Sellers | 76% | 9.1<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 6.4 |
| Dailyn Swain | 67% | 8.0<br><sub>-,-,2,6,-</sub> | 3.2<br><sub>-,-,0,2,-</sub> |  | 1.2<br><sub>-,-,1,1,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.1 |

</details>


### PHX @ NOP
Out: Bennedict Mathurin (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Mark Williams (PHX)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 121.6–115.6 | PHX 67% | 1.50 / 2.99 | NOP +6.5 | 237.5 | NOP +3.5 covers 42%; o233.5 57% |
| Expected (weighted by chance each plays) | 121.5–115.7 | PHX 66% | 1.52 / 2.93 | NOP +5.5 | 236.5 | NOP +3.5 covers 43%; o233.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Dunn (PHX) | Questionable | 55% | 13.7 | 4.2 | 3.3 | 0.9 | 0.4 | 0.6 | 0.4 | 0.4 | 8.4 | small |
| Malik Dia (NOP) | Questionable | 55% | 5.7 | 2.3 | 0.7 | 0.8 | 0.2 | 0.2 | 0.2 | 0.3 | 3.8 | small |
| Julian Reese (NOP) | Questionable | 55% | 5.6 | 1.9 | 1.1 | 0.3 | 0.0 | 0.2 | 0.3 | 0.3 | 3.3 | small |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 99% | 36.3<br><sub>35,28,37,33,38</sub> | 27.8<br><sub>30,17,20,29,23</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>1,4,4,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 6.4<br><sub>7,7,8,6,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>4,0,1,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.3 | 2.9 | 37.6 |
| Dillon Brooks | 99% | 30.1<br><sub>30,22,27,31,25</sub> | 17.0<br><sub>15,1,15,29,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>3,2,4,3,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>1,0,4,5,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.2<br><sub>3,0,3,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 23.1 |
| Miles Bridges | 99% | 29.2<br><sub>25,24,29,29,25</sub> | 14.8<br><sub>11,14,16,13,18</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>6,3,8,6,9</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,3,2,5,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.7 | 1.1 | 24.7 |
| Jalen Green | 98% | 28.1<br><sub>21,21,27,30,25</sub> | 16.1<br><sub>12,9,16,18,14</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>4,2,5,7,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>0,1,3,7,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,1,2,4,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.4 | 2.2 | 23.3 |
| Oso Ighodaro | 98% | 26.2<br><sub>32,17,33,21,27</sub> | 7.2<br><sub>2,4,8,7,3</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>3,2,11,4,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>7,3,3,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.9 | 1.3 | 17.3 |
| Collin Gillespie | 99% | 25.6<br><sub>27,28,26,17,27</sub> | 10.7<br><sub>13,26,10,9,16</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,4,3,3,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.0<br><sub>1,4,3,1,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>3,5,2,2,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.2 | 1.2 | 18.0 |
| Jordan Goodwin | 98% | 22.8<br><sub>24,31,20,17,28</sub> | 8.9<br><sub>6,14,11,2,5</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>5,7,6,5,9</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,6,2,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,1,1,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.2 | 0.8 | 16.4 |
| Luke Kennard | 98% | 17.5<br><sub>21,23,17,17,15</sub> | 7.2<br><sub>8,18,12,3,5</sub> |  | 1.9<br><sub>1,6,2,3,0</sub> |  | 1.6<br><sub>1,4,0,1,0</sub> |  | 1.0<br><sub>0,3,4,1,1</sub> |  | 0.5 | 0.1 | 0.6 | 10.7 |
| Khaman Maluach | 98% | 16.9<br><sub>16,13,11,21,18</sub> | 6.7<br><sub>4,7,4,10,9</sub> |  | 5.7<br><sub>2,4,6,2,6</sub> |  | 0.8<br><sub>1,0,0,0,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.2 | 1.0 | 13.1 |
| Rasheer Fleming | 48% | 8.6<br><sub>-,-,-,4,-</sub> | 3.2<br><sub>-,-,-,0,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 5.2 |
| Drew Timme | 5% | 7.7 | 3.0 |  | 1.4 |  | 0.7 |  | 0.2 |  | 0.2 | 0.1 | 0.4 | 5.2 |
| Jamaree Bouyea | 52% | 7.2<br><sub>-,-,-,4,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 0.9<br><sub>-,-,-,1,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 4.8 |
| Pat Spencer | 48% | 7.1<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Koa Peat | 80% | 7.0<br><sub>-,8,1,4,3</sub> | 3.4<br><sub>-,10,0,2,0</sub> |  | 1.6<br><sub>-,2,1,0,0</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.3 | 0.3 | 5.3 |
| Duop Reath | 48% | 6.7<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.6 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 92% | 31.8<br><sub>-,-,-,29,-</sub> | 16.2<br><sub>-,-,-,17,-</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>-,-,-,4,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,-,-,1,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>-,-,-,3,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.4 | 1.6 | 24.7 |
| Saddiq Bey | 98% | 31.5<br><sub>41,33,42,37,32</sub> | 15.8<br><sub>16,23,10,21,2</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>6,6,8,6,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>4,3,6,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>2,5,2,4,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.2 | 1.1 | 23.5 |
| Jeremiah Fears | 99% | 31.0<br><sub>33,29,31,38,34</sub> | 17.9<br><sub>13,19,16,22,29</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>4,10,5,7,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>7,10,4,5,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.5 | 3.1 | 28.5 |
| Zion Williamson | 70% | 30.7<br><sub>31,25,32,37,-</sub> | 19.8<br><sub>24,16,24,22,-</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>6,6,7,6,-</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,2,1,7,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.2<br><sub>2,0,0,0,-</sub> |  | 1.2 | 0.6 | 2.3 | 28.8 |
| Herbert Jones | 98% | 25.1<br><sub>27,24,32,33,25</sub> | 8.2<br><sub>10,8,9,14,2</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>2,2,1,2,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,3,3,3,2</sub> |  | 1.1<br><sub>2,2,3,4,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.4 | 1.3 | 13.4 |
| Derik Queen | 99% | 24.8<br><sub>25,21,19,18,35</sub> | 12.7<br><sub>10,17,9,11,15</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>5,10,5,7,15</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 2.9<br><sub>4,0,0,3,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.5<br><sub>2,4,0,0,0</sub> |  | 0.9 | 0.8 | 2.5 | 23.0 |
| Yves Missi | 98% | 24.4<br><sub>22,23,17,23,35</sub> | 7.5<br><sub>3,6,4,4,9</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 8.2<br><sub>8,14,5,7,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,1,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.6 | 1.2 | 17.2 |
| Jordan Poole | 88% | 23.7<br><sub>24,31,30,13,31</sub> | 12.9<br><sub>14,11,22,6,25</sub> |  | 2.3<br><sub>2,2,1,0,3</sub> |  | 3.4<br><sub>5,5,5,1,2</sub> |  | 1.9<br><sub>1,1,3,2,3</sub> |  | 0.7 | 0.3 | 1.8 | 18.6 |
| Jaron Pierre Jr. | 90% | 15.3<br><sub>23,19,17,4,25</sub> | 6.8<br><sub>13,10,7,3,6</sub> |  | 2.2<br><sub>2,4,1,2,5</sub> |  | 0.9<br><sub>0,0,1,0,0</sub> |  | 0.8<br><sub>2,2,1,1,2</sub> |  | 0.4 | 0.2 | 0.9 | 10.0 |
| Karlo Matkovic | 98% | 15.0<br><sub>14,20,10,8,15</sub> | 5.3<br><sub>5,3,0,0,3</sub> |  | 3.3<br><sub>3,2,2,2,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.5<br><sub>1,0,0,0,1</sub> |  | 0.5 | 0.6 | 0.8 | 9.4 |
| Bryce McGowens | 62% | 9.3<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.1 |
| DeAndre Jordan | 38% | 8.7<br><sub>-,-,10,-,-</sub> | 2.6<br><sub>-,-,8,-,-</sub> |  | 3.5<br><sub>-,-,2,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.7 |
| AJ Johnson | 52% | 6.4<br><sub>-,6,-,-,8</sub> | 2.2<br><sub>-,0,-,-,0</sub> |  | 0.8<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.5 |

</details>


### LAC @ HOU
Out: Bradley Beal (LAC)

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 99% | 32.5<br><sub>37,35,30,35,32</sub> | 20.7<br><sub>24,27,20,23,16</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,6,3,0,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>7,7,7,5,2</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>3,3,2,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 3.4 | 29.5 |
| Rui Hachimura | 98% | 28.5<br><sub>32,22,27,32,29</sub> | 13.4<br><sub>7,4,20,17,19</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>11,2,5,7,8</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>3,0,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.7<br><sub>1,0,4,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 1.2 | 19.1 |
| Derrick Jones Jr. | 98% | 26.8<br><sub>29,26,28,27,26</sub> | 9.4<br><sub>14,13,5,8,4</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>5,4,1,2,7</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>0,1,1,1,1</sub> |  | 1.0<br><sub>4,3,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.0 | 0.8 | 0.9 | 14.2 |
| Brook Lopez | 99% | 25.1<br><sub>31,29,23,27,25</sub> | 13.2<br><sub>26,7,23,23,21</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>7,5,6,3,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>4,8,2,4,0</sub> |  | 1.5<br><sub>3,1,4,5,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.7 | 1.1 | 1.2 | 19.6 |
| Max Strus | 98% | 24.6<br><sub>23,25,21,32,29</sub> | 9.0<br><sub>3,14,3,18,5</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>2,3,2,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.5<br><sub>3,4,1,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,4,1,5,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.1 | 1.1 | 15.3 |
| Brandon Ingram | 8% | 22.3 | 12.8 | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.2 | 3.5<br><sub>o 41% · u 59%</sub> | 2.1 | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.4 | 1.7 | 18.1 |
| Kris Dunn | 99% | 22.0<br><sub>20,18,26,20,19</sub> | 5.9<br><sub>2,7,2,6,3</sub> |  | 2.8<br><sub>3,3,5,2,4</sub> |  | 3.1<br><sub>6,1,5,2,5</sub> |  | 0.6<br><sub>0,0,0,1,1</sub> |  | 1.5 | 0.2 | 1.0 | 11.9 |
| Keaton Wagler | 98% | 19.9<br><sub>18,28,18,17,19</sub> | 10.0<br><sub>14,12,15,7,7</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,4,2,5,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>1,5,0,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1<br><sub>2,2,1,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.7 | 0.2 | 1.7 | 15.2 |
| Kobe Sanders | 98% | 18.5<br><sub>15,20,18,14,19</sub> | 6.8<br><sub>5,2,5,0,9</sub> |  | 2.0<br><sub>0,6,1,1,3</sub> |  | 1.7<br><sub>1,4,3,1,1</sub> |  | 0.9<br><sub>1,0,0,0,3</sub> |  | 0.8 | 0.2 | 1.1 | 10.5 |
| Gradey Dick | 98% | 15.0<br><sub>19,19,17,13,16</sub> | 6.4<br><sub>13,12,0,2,6</sub> |  | 2.2<br><sub>3,2,0,2,5</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.5<br><sub>2,2,0,0,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.2 |
| Yanic Konan Niederhauser | 64% | 12.9<br><sub>-,-,-,11,16</sub> | 4.2<br><sub>-,-,-,2,6</sub> |  | 3.5<br><sub>-,-,-,3,6</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.6 | 0.9 | 8.4 |
| Isaiah Jackson | 98% | 12.0<br><sub>17,15,19,9,4</sub> | 5.0<br><sub>5,13,8,6,0</sub> |  | 3.4<br><sub>3,2,5,4,0</sub> |  | 0.9<br><sub>3,2,0,2,0</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.6 | 0.7 | 0.8 | 9.3 |
| Baba Miller | 88% | 8.6<br><sub>-,5,4,1,3</sub> | 4.1<br><sub>-,2,3,0,1</sub> |  | 1.2<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 0.2<br><sub>-,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.2 |
| Jalen Pickett | 52% | 6.4<br><sub>-,-,-,1,-</sub> | 2.4<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Blake Wesley | 52% | 6.0<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.1 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 99% | 36.1<br><sub>33,30,29,32,35</sub> | 23.0<br><sub>22,25,22,21,16</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,4,2,2,4</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 4.9<br><sub>6,5,3,3,4</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,2,2,4,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.9 | 3.2 | 33.5 |
| Amen Thompson | 88% | 34.9<br><sub>41,29,-,31,26</sub> | 17.3<br><sub>12,26,-,15,22</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>10,7,-,9,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>3,7,-,3,0</sub> | 2.5<br><sub>o 63% · u 37%</sub> | 0.3<br><sub>0,3,-,0,0</sub> |  | 1.5 | 0.7 | 2.2 | 29.0 |
| Jabari Smith Jr. | 99% | 34.7<br><sub>24,28,32,26,32</sub> | 15.5<br><sub>6,9,12,17,21</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>3,6,10,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>0,5,1,2,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.9 | 1.3 | 24.4 |
| Alperen Sengun | 96% | 34.4<br><sub>37,28,30,14,36</sub> | 21.5<br><sub>43,19,23,7,28</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 9.5<br><sub>12,8,7,7,11</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>5,8,2,1,10</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.2 | 1.0 | 3.0 | 37.9 |
| Fred VanVleet | 88% | 32.8<br><sub>34,-,26,27,33</sub> | 14.1<br><sub>17,-,8,15,25</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>2,-,5,2,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 5.6<br><sub>3,-,6,6,9</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>3,-,2,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.4 | 1.5 | 22.9 |
| Tari Eason | 99% | 24.2<br><sub>33,30,27,25,23</sub> | 9.8<br><sub>14,25,7,11,7</sub> |  | 5.7<br><sub>11,7,7,4,6</sub> |  | 1.5<br><sub>2,1,3,3,1</sub> |  | 1.1<br><sub>2,3,0,1,1</sub> |  | 1.2 | 0.6 | 1.1 | 16.9 |
| Marcus Smart | 64% | 19.7<br><sub>-,-,-,18,23</sub> | 7.0<br><sub>-,-,-,4,3</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>-,-,-,2,2</sub> |  | 2.2<br><sub>-,-,-,4,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0<br><sub>-,-,-,1,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.1 | 0.3 | 1.3 | 11.2 |
| Reed Sheppard | 93% | 18.3<br><sub>19,26,19,25,14</sub> | 8.4<br><sub>0,11,5,20,0</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>0,1,2,4,2</sub> |  | 2.2<br><sub>3,6,2,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>0,3,1,6,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.4 | 0.9 | 12.3 |
| Steven Adams | 52% | 13.2<br><sub>-,12,-,16,12</sub> | 3.7<br><sub>-,6,-,4,2</sub> |  | 4.7<br><sub>-,7,-,5,2</sub> |  | 0.9<br><sub>-,1,-,2,2</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 9.3 |
| Bogdan Bogdanovic | 98% | 11.0<br><sub>12,22,26,11,5</sub> | 4.2<br><sub>11,12,6,1,0</sub> |  | 1.3<br><sub>1,3,0,3,1</sub> |  | 1.0<br><sub>3,4,1,0,0</sub> |  | 0.6<br><sub>3,2,2,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.5 |
| Clint Capela | 38% | 9.4<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 3.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.6 | 0.5 | 7.0 |
| Oscar Tshiebwe | 72% | 7.5<br><sub>6,12,6,11,-</sub> | 3.3<br><sub>0,4,6,4,-</sub> |  | 3.1<br><sub>5,9,6,4,-</sub> |  | 0.5<br><sub>0,3,0,3,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.9 |
| Isaiah Crawford | 63% | 6.2<br><sub>-,9,21,2,-</sub> | 2.2<br><sub>-,4,11,0,-</sub> |  | 1.4<br><sub>-,2,10,0,-</sub> |  | 0.3<br><sub>-,0,3,0,-</sub> |  | 0.1<br><sub>-,0,1,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.8 |
| Jae'Sean Tate | 58% | 5.9<br><sub>-,8,12,1,-</sub> | 1.8<br><sub>-,4,3,0,-</sub> |  | 1.4<br><sub>-,2,3,0,-</sub> |  | 0.4<br><sub>-,0,2,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.7 |
| Bruce Thornton | 72% | 5.6<br><sub>-,6,12,1,-</sub> | 2.6<br><sub>-,2,7,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.3 |

</details>


### UTA @ LAL
Out: Austin Reaves (LAL), Jaxson Hayes (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 35.2<br><sub>38,34,35,39,36</sub> | 22.3<br><sub>27,13,30,30,14</sub> |  | 3.7<br><sub>4,4,2,1,3</sub> |  | 7.0<br><sub>7,8,11,10,6</sub> |  | 2.5<br><sub>4,1,4,5,0</sub> |  | 1.0 | 0.2 | 3.7 | 33.0 |
| Darryn Peterson | 98% | 32.1<br><sub>34,34,31,19,32</sub> | 17.8<br><sub>28,17,13,11,20</sub> |  | 4.5<br><sub>7,5,5,1,10</sub> |  | 4.4<br><sub>2,4,2,3,8</sub> |  | 2.1<br><sub>4,3,2,1,0</sub> |  | 1.2 | 0.5 | 2.4 | 26.7 |
| Ace Bailey | 99% | 31.6<br><sub>35,30,23,27,24</sub> | 15.8<br><sub>21,7,5,19,7</sub> |  | 5.4<br><sub>3,8,1,8,7</sub> |  | 2.3<br><sub>1,4,4,3,1</sub> |  | 2.1<br><sub>3,1,1,2,0</sub> |  | 1.0 | 0.8 | 2.0 | 23.5 |
| Josh Green | 97% | 26.8<br><sub>14,15,13,28,29</sub> | 6.2<br><sub>2,6,9,11,8</sub> |  | 2.5<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.9<br><sub>0,2,1,2,2</sub> |  | 0.9 | 0.2 | 1.0 | 10.0 |
| Brice Sensabaugh | 99% | 25.9<br><sub>27,30,35,14,26</sub> | 15.7<br><sub>7,14,40,8,18</sub> |  | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.5<br><sub>1,0,8,0,5</sub> |  | 0.7 | 0.2 | 2.3 | 21.9 |
| Svi Mykhailiuk | 98% | 25.2<br><sub>7,21,33,34,28</sub> | 9.2<br><sub>0,6,8,15,11</sub> |  | 2.8<br><sub>1,2,7,3,7</sub> |  | 2.2<br><sub>0,3,5,5,2</sub> |  | 1.6<br><sub>0,2,2,4,3</sub> |  | 0.7 | 0.1 | 1.2 | 14.2 |
| Mo Bamba | 91% | 22.9<br><sub>20,36,31,23,20</sub> | 7.8<br><sub>9,26,15,6,2</sub> |  | 7.7<br><sub>9,5,10,16,2</sub> |  | 1.0<br><sub>1,4,3,0,0</sub> |  | 0.5<br><sub>0,6,1,0,0</sub> |  | 0.6 | 1.3 | 1.0 | 16.4 |
| Josh Okogie | 98% | 22.5<br><sub>22,27,22,15,17</sub> | 6.2<br><sub>7,7,9,3,3</sub> |  | 3.4<br><sub>2,6,2,0,2</sub> |  | 1.3<br><sub>1,0,4,0,2</sub> |  | 0.7<br><sub>2,2,1,0,0</sub> |  | 1.2 | 0.2 | 0.9 | 10.8 |
| Isaiah Collier | 58% | 16.7<br><sub>16,-,-,10,-</sub> | 7.7<br><sub>3,-,-,0,-</sub> |  | 2.3<br><sub>2,-,-,1,-</sub> |  | 4.4<br><sub>5,-,-,2,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.8 | 0.2 | 1.7 | 14.4 |
| Kyle Filipowski | 52% | 14.2<br><sub>2,-,-,6,-</sub> | 7.0<br><sub>2,-,-,0,-</sub> |  | 4.3<br><sub>0,-,-,3,-</sub> |  | 1.4<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.6 | 0.2 | 1.0 | 12.6 |
| Tony Bradley | 52% | 12.9<br><sub>12,12,17,-,-</sub> | 4.0<br><sub>0,6,3,-,-</sub> |  | 4.0<br><sub>5,2,7,-,-</sub> |  | 0.6<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.3 | 0.6 | 8.6 |
| Kobe Bufkin | 23% | 11.5<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.7 | 7.8 |
| Jonas Aidoo | 30% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Harrison Ingram | 8% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 99% | 35.4<br><sub>32,36,42,37,36</sub> | 39.5<br><sub>32,43,36,29,25</sub> |  | 6.8<br><sub>5,3,6,5,4</sub> |  | 8.2<br><sub>5,9,7,7,8</sub> |  | 4.9<br><sub>5,5,5,2,2</sub> |  | 1.9 | 0.6 | 4.3 | 54.5 |
| Quentin Grimes | 99% | 30.6<br><sub>-,37,42,35,35</sub> | 14.2<br><sub>-,22,47,20,13</sub> |  | 3.9<br><sub>-,6,6,7,5</sub> |  | 3.3<br><sub>-,1,3,4,7</sub> |  | 1.9<br><sub>-,5,10,4,1</sub> |  | 1.1 | 0.3 | 1.5 | 21.3 |
| Walker Kessler | 99% | 29.4<br><sub>29,32,-,31,30</sub> | 12.9<br><sub>10,14,-,10,15</sub> |  | 11.4<br><sub>11,12,-,11,7</sub> |  | 1.9<br><sub>3,3,-,1,2</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.9 | 2.4 | 1.6 | 26.2 |
| Jake LaRavia | 98% | 24.3<br><sub>21,32,23,30,24</sub> | 6.8<br><sub>0,12,4,4,6</sub> |  | 4.3<br><sub>9,3,5,6,3</sub> |  | 2.0<br><sub>6,3,2,2,0</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 1.2 | 0.6 | 1.1 | 13.1 |
| Matisse Thybulle | 98% | 24.3<br><sub>23,26,31,21,27</sub> | 7.4<br><sub>8,12,7,2,14</sub> |  | 2.8<br><sub>5,8,6,1,1</sub> |  | 1.3<br><sub>1,0,0,3,1</sub> |  | 1.3<br><sub>2,2,2,0,4</sub> |  | 2.5 | 0.9 | 1.1 | 11.5 |
| Ziaire Williams | 98% | 22.7<br><sub>20,19,24,18,28</sub> | 9.2<br><sub>9,6,0,7,5</sub> |  | 2.4<br><sub>1,2,1,2,0</sub> |  | 1.4<br><sub>5,3,1,0,1</sub> |  | 1.2<br><sub>1,0,0,1,1</sub> |  | 1.3 | 0.3 | 0.8 | 12.9 |
| Sandro Mamukelashvili | 99% | 21.0<br><sub>26,21,23,21,20</sub> | 9.9<br><sub>23,4,3,6,9</sub> |  | 4.7<br><sub>3,2,3,3,9</sub> |  | 1.7<br><sub>2,3,2,0,2</sub> |  | 1.2<br><sub>5,0,0,0,0</sub> |  | 0.8 | 0.4 | 0.8 | 16.3 |
| Collin Sexton | 99% | 20.2<br><sub>13,24,25,20,18</sub> | 13.0<br><sub>10,16,10,12,10</sub> |  | 2.0<br><sub>1,0,4,0,1</sub> |  | 2.8<br><sub>3,3,3,1,4</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 0.9 | 0.2 | 1.6 | 17.8 |
| Jarred Vanderbilt | 91% | 12.4<br><sub>9,12,14,12,10</sub> | 3.1<br><sub>4,2,4,0,4</sub> |  | 3.9<br><sub>3,4,7,5,4</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.1 |
| Cameron Carr | 72% | 8.6<br><sub>13,-,-,2,12</sub> | 3.7<br><sub>0,-,-,5,5</sub> |  | 1.3<br><sub>2,-,-,0,1</sub> |  | 0.5<br><sub>0,-,-,1,0</sub> |  | 0.4<br><sub>0,-,-,1,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 38% | 7.9<br><sub>4,-,17,-,-</sub> | 1.8<br><sub>0,-,4,-,-</sub> |  | 3.0<br><sub>2,-,8,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 5.3 |
| Carson Cooper | 58% | 7.1<br><sub>-,-,18,2,-</sub> | 2.4<br><sub>-,-,3,2,-</sub> |  | 2.1<br><sub>-,-,4,1,-</sub> |  | 0.5<br><sub>-,-,2,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 5.0 |
| Adou Thiero | 64% | 7.1<br><sub>14,-,6,6,-</sub> | 2.3<br><sub>2,-,0,0,-</sub> |  | 1.8<br><sub>2,-,0,1,-</sub> |  | 0.6<br><sub>1,-,1,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Jaden Hardy | 52% | 6.7<br><sub>4,-,-,2,-</sub> | 3.6<br><sub>3,-,-,0,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.6<br><sub>0,-,-,1,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Bronny James | 52% | 5.4<br><sub>4,-,-,2,-</sub> | 2.0<br><sub>4,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.5 |
| Chris Manon | 52% | 5.4<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.2 |

</details>


### SAS @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Dylan Harper (SAS), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.7–108.9 | SAS 71% | 1.41 / 3.43 | SAC +7.5 | 225.5 | SAC +10.5 covers 58%; o224.5 52% |
| Expected (weighted by chance each plays) | 118.6–108.3 | SAS 77% | 1.30 / 4.30 | SAC +10.5 | 226.5 | SAC +10.5 covers 51%; o224.5 55% |
| if De'Aaron Fox plays | 117.9–109.1 | SAS 73% | 1.36 / 3.74 | SAC +8.5 | 227.5 | SAC +10.5 covers 55%; o224.5 55% |
| if Victor Wembanyama plays | 118.7–108.0 | SAS 78% | 1.29 / 4.45 | SAC +10.5 | 226.5 | SAC +10.5 covers 50%; o224.5 55% |
| if Jordan McLaughlin plays | 117.4–109.5 | SAS 71% | 1.41 / 3.47 | SAC +7.5 | 226.5 | SAC +10.5 covers 57%; o224.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 31.9 | 18.6 | 4.2 | 7.1 | 1.5 | 1.5 | 0.3 | 2.5 | 29.9 | full tables below |
| Victor Wembanyama (SAS) | Questionable | 55% | 32.3 | 31.7 | 12.2 | 4.6 | 2.4 | 1.2 | 3.3 | 2.7 | 48.4 | full tables below |
| Jordan McLaughlin (SAS) | Questionable | 55% | 25.2 | 8.6 | 3.6 | 4.9 | 1.1 | 1.9 | 0.2 | 1.2 | 17.1 | full tables below |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephon Castle | 99% | 32.3<br><sub>25,35,31,33,29</sub> | 24.0<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 8.3<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>5,0,2,2,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.3 | 37.9 |
| Devin Vassell | 99% | 32.2<br><sub>23,32,36,32,26</sub> | 17.7<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>2,6,5,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.9<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.5 | 1.5 | 26.1 |
| Julian Champagnie | 99% | 29.7<br><sub>23,24,30,29,25</sub> | 14.4<br><sub>7,4,14,20,9</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>8,5,6,4,3</sub> |  | 2.2<br><sub>3,1,0,1,3</sub> |  | 2.6<br><sub>1,1,4,4,3</sub> |  | 1.1 | 0.5 | 1.0 | 21.8 |
| Keldon Johnson | 99% | 28.4<br><sub>25,29,15,27,23</sub> | 15.4<br><sub>18,11,4,10,10</sub> |  | 6.0<br><sub>4,10,2,5,4</sub> |  | 3.0<br><sub>4,2,1,3,4</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.4 | 24.5 |
| Harrison Barnes | 93% | 26.8<br><sub>21,14,10,16,21</sub> | 11.4<br><sub>11,0,0,9,3</sub> |  | 3.1<br><sub>1,0,3,2,5</sub> |  | 1.9<br><sub>1,2,4,1,2</sub> |  | 1.7<br><sub>3,0,0,1,0</sub> |  | 0.7 | 0.2 | 1.0 | 16.5 |
| Carter Bryant | 96% | 26.7<br><sub>19,5,2,13,20</sub> | 11.3<br><sub>8,0,0,3,8</sub> |  | 4.1<br><sub>3,1,0,1,3</sub> |  | 1.8<br><sub>2,0,0,0,0</sub> |  | 1.9<br><sub>2,0,0,1,2</sub> |  | 0.6 | 0.6 | 1.1 | 17.2 |
| Luke Kornet | 99% | 20.5<br><sub>16,13,14,15,10</sub> | 5.8<br><sub>6,2,2,4,0</sub> |  | 5.9<br><sub>7,2,1,0,3</sub> |  | 1.9<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.9 | 0.7 | 13.6 |
| Tarris Reed Jr. | 58% | 18.6<br><sub>11,-,-,-,6</sub> | 6.6<br><sub>2,-,-,-,0</sub> |  | 7.2<br><sub>4,-,-,-,4</sub> |  | 1.1<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.6 | 1.1 | 14.9 |
| David Jones Garcia | 58% | 16.7<br><sub>-,-,-,-,4</sub> | 7.2<br><sub>-,-,-,-,0</sub> |  | 2.7<br><sub>-,-,-,-,1</sub> |  | 2.6<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 1.1 | 0.3 | 0.9 | 12.4 |
| Maliq Brown | 80% | 13.8<br><sub>-,-,-,-,-</sub> | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 5.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 6.2 |
| Ja'Kobi Gillespie | 88% | 13.7<br><sub>-,-,-,-,-</sub> | 10.8<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.6 | 12.3 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 36.1<br><sub>35,33,35,36,40</sub> | 24.0<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 3.6 | 35.5 |
| De'Andre Hunter | 88% | 32.9<br><sub>42,-,35,37,41</sub> | 13.4<br><sub>24,-,7,30,20</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,-,1,6,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 19.9 |
| Keegan Murray | 98% | 31.4<br><sub>40,21,31,40,40</sub> | 11.7<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.9 | 0.9 | 18.3 |
| Zach LaVine | 88% | 31.3<br><sub>36,-,32,39,30</sub> | 16.9<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.2 | 2.0 | 23.0 |
| Domantas Sabonis | 99% | 30.9<br><sub>35,29,24,38,32</sub> | 14.5<br><sub>21,11,8,19,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 11.6<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 23% · u 77%</sub> | 0.7 | 0.2 | 2.2 | 31.1 |
| Precious Achiuwa | 98% | 21.2<br><sub>-,-,8,-,22</sub> | 9.0<br><sub>-,-,0,-,5</sub> |  | 5.6<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.7 |
| Malik Monk | 98% | 14.9<br><sub>18,29,20,12,10</sub> | 7.7<br><sub>7,14,8,2,3</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 2.8<br><sub>3,10,2,3,1</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.3 | 1.1 | 11.9 |
| Emanuel Sharp | 98% | 14.3<br><sub>7,21,14,10,16</sub> | 4.6<br><sub>4,9,6,3,3</sub> |  | 1.2<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.5 |
| Leaky Black | 91% | 13.3<br><sub>12,29,17,19,4</sub> | 2.9<br><sub>0,12,3,0,2</sub> |  | 2.1<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.6 | 0.3 | 0.3 | 5.8 |
| Dylan Cardwell | 98% | 12.1<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.2<br><sub>3,6,4,4,1</sub> |  | 0.9<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 8.9 |
| Alex Karaban | 48% | 8.0<br><sub>-,29,4,-,-</sub> | 1.6<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |
| Daeqwon Plowden | 58% | 7.9<br><sub>2,24,4,-,-</sub> | 2.8<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Mason Plumlee | 48% | 6.3<br><sub>-,5,4,-,-</sub> | 2.0<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.6 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. (SAC) | 98% | 36.1<br><sub>35,33,35,36,40</sub> | 24.0<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 3.6 | 35.5 |
| De'Andre Hunter (SAC) | 88% | 32.9<br><sub>42,-,35,37,41</sub> | 13.4<br><sub>24,-,7,30,20</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,-,1,6,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 19.8 |
| Keegan Murray (SAC) | 98% | 31.4<br><sub>40,21,31,40,40</sub> | 11.7<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.9 | 0.9 | 18.4 |
| Zach LaVine (SAC) | 88% | 31.1<br><sub>36,-,32,39,30</sub> | 16.9<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.2 | 2.0 | 23.0 |
| Domantas Sabonis (SAC) | 99% | 30.8<br><sub>35,29,24,38,32</sub> | 14.5<br><sub>21,11,8,19,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 11.6<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 23% · u 77%</sub> | 0.7 | 0.2 | 2.3 | 31.0 |
| Precious Achiuwa (SAC) | 98% | 21.2<br><sub>-,-,8,-,22</sub> | 9.0<br><sub>-,-,0,-,5</sub> |  | 5.6<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.7 |
| Malik Monk (SAC) | 98% | 14.8<br><sub>18,29,20,12,10</sub> | 7.7<br><sub>7,14,8,2,3</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 2.8<br><sub>3,10,2,3,1</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.3 | 1.1 | 11.9 |
| Emanuel Sharp (SAC) | 98% | 14.3<br><sub>7,21,14,10,16</sub> | 4.6<br><sub>4,9,6,3,3</sub> |  | 1.2<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.5 |
| Leaky Black (SAC) | 91% | 13.2<br><sub>12,29,17,19,4</sub> | 2.9<br><sub>0,12,3,0,2</sub> |  | 2.1<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.6 | 0.3 | 0.3 | 5.8 |
| Dylan Cardwell (SAC) | 98% | 12.1<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.1<br><sub>3,6,4,4,1</sub> |  | 0.9<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 8.9 |
| Alex Karaban (SAC) | 48% | 8.0<br><sub>-,29,4,-,-</sub> | 1.6<br><sub>-,0,0,-,-</sub> |  | 1.2<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |
| Daeqwon Plowden (SAC) | 58% | 8.0<br><sub>2,24,4,-,-</sub> | 2.9<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Mason Plumlee (SAC) | 48% | 6.2<br><sub>-,5,4,-,-</sub> | 1.9<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.5 |
| Devin Vassell (SAS) | 99% | 32.6<br><sub>23,32,36,32,26</sub> | 16.8<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>2,6,5,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.6<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.4 | 1.2 | 25.0 |
| Stephon Castle (SAS) | 99% | 32.3<br><sub>25,35,31,33,29</sub> | 22.2<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 7.5<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>5,0,2,2,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.0 | 35.2 |
| De'Aaron Fox (SAS) | 100% | 31.9<br><sub>17,-,34,32,26</sub> | 18.6<br><sub>7,-,6,10,5</sub> | 15.5 · – | 4.2<br><sub>5,-,2,2,2</sub> | 3.5 | 7.1<br><sub>1,-,2,5,10</sub> | 6.5 | 1.5<br><sub>0,-,0,0,0</sub> | 1.5 | 1.5 | 0.3 | 2.5 | 29.9 |
| Julian Champagnie (SAS) | 99% | 29.8<br><sub>23,24,30,29,25</sub> | 13.3<br><sub>7,4,14,20,9</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>8,5,6,4,3</sub> |  | 2.0<br><sub>3,1,0,1,3</sub> |  | 2.5<br><sub>1,1,4,4,3</sub> |  | 1.1 | 0.5 | 0.8 | 20.5 |
| Keldon Johnson (SAS) | 99% | 28.0<br><sub>25,29,15,27,23</sub> | 14.2<br><sub>18,11,4,10,10</sub> |  | 6.1<br><sub>4,10,2,5,4</sub> |  | 2.7<br><sub>4,2,1,3,4</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.2 | 23.0 |
| Harrison Barnes (SAS) | 93% | 24.0<br><sub>21,14,10,16,21</sub> | 9.6<br><sub>11,0,0,9,3</sub> |  | 2.8<br><sub>1,0,3,2,5</sub> |  | 1.6<br><sub>1,2,4,1,2</sub> |  | 1.4<br><sub>3,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.7 | 14.0 |
| Carter Bryant (SAS) | 96% | 21.3<br><sub>19,5,2,13,20</sub> | 8.5<br><sub>8,0,0,3,8</sub> |  | 3.3<br><sub>3,1,0,1,3</sub> |  | 1.4<br><sub>2,0,0,0,0</sub> |  | 1.4<br><sub>2,0,0,1,2</sub> |  | 0.5 | 0.5 | 0.8 | 13.1 |
| Luke Kornet (SAS) | 99% | 18.1<br><sub>16,13,14,15,10</sub> | 4.9<br><sub>6,2,2,4,0</sub> |  | 5.2<br><sub>7,2,1,0,3</sub> |  | 1.5<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.6 | 11.6 |
| Tarris Reed Jr. (SAS) | 58% | 12.6<br><sub>11,-,-,-,6</sub> | 4.4<br><sub>2,-,-,-,0</sub> |  | 4.8<br><sub>4,-,-,-,4</sub> |  | 0.7<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.7 | 9.9 |
| David Jones Garcia (SAS) | 58% | 11.9<br><sub>-,-,-,-,4</sub> | 4.7<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,1</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.2 | 0.6 | 8.4 |
| Maliq Brown (SAS) | 80% | 10.1<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.6 |
| Ja'Kobi Gillespie (SAS) | 88% | 8.7<br><sub>-,-,-,-,-</sub> | 6.8<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 7.8 |

</details>

<details><summary>if Jordan McLaughlin plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. (SAC) | 98% | 36.1<br><sub>35,33,35,36,40</sub> | 24.0<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 3.6 | 35.5 |
| De'Andre Hunter (SAC) | 88% | 32.9<br><sub>42,-,35,37,41</sub> | 13.5<br><sub>24,-,7,30,20</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,-,1,6,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 19.8 |
| Keegan Murray (SAC) | 98% | 31.5<br><sub>40,21,31,40,40</sub> | 11.7<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.9 | 0.9 | 18.4 |
| Zach LaVine (SAC) | 88% | 31.3<br><sub>36,-,32,39,30</sub> | 17.0<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.2 | 2.0 | 23.1 |
| Domantas Sabonis (SAC) | 99% | 30.8<br><sub>35,29,24,38,32</sub> | 14.5<br><sub>21,11,8,19,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 11.6<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 23% · u 77%</sub> | 0.7 | 0.2 | 2.2 | 31.0 |
| Precious Achiuwa (SAC) | 98% | 21.2<br><sub>-,-,8,-,22</sub> | 9.1<br><sub>-,-,0,-,5</sub> |  | 5.6<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.8 |
| Malik Monk (SAC) | 98% | 14.9<br><sub>18,29,20,12,10</sub> | 7.7<br><sub>7,14,8,2,3</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 2.8<br><sub>3,10,2,3,1</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.3 | 1.1 | 11.9 |
| Emanuel Sharp (SAC) | 98% | 14.4<br><sub>7,21,14,10,16</sub> | 4.7<br><sub>4,9,6,3,3</sub> |  | 1.2<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Leaky Black (SAC) | 91% | 13.3<br><sub>12,29,17,19,4</sub> | 2.9<br><sub>0,12,3,0,2</sub> |  | 2.1<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.6 | 0.3 | 0.3 | 5.9 |
| Dylan Cardwell (SAC) | 98% | 12.0<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.1<br><sub>3,6,4,4,1</sub> |  | 0.9<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 8.8 |
| Alex Karaban (SAC) | 48% | 8.0<br><sub>-,29,4,-,-</sub> | 1.6<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |
| Daeqwon Plowden (SAC) | 58% | 7.8<br><sub>2,24,4,-,-</sub> | 2.8<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Mason Plumlee (SAC) | 48% | 6.2<br><sub>-,5,4,-,-</sub> | 1.9<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.6 |
| Stephon Castle (SAS) | 99% | 32.0<br><sub>25,35,31,33,29</sub> | 23.2<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 7.8<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>5,0,2,2,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.2 | 36.5 |
| Devin Vassell (SAS) | 99% | 32.0<br><sub>23,32,36,32,26</sub> | 17.2<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>2,6,5,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.8<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.4 | 1.4 | 25.4 |
| Julian Champagnie (SAS) | 99% | 29.5<br><sub>23,24,30,29,25</sub> | 14.1<br><sub>7,4,14,20,9</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>8,5,6,4,3</sub> |  | 2.1<br><sub>3,1,0,1,3</sub> |  | 2.5<br><sub>1,1,4,4,3</sub> |  | 1.1 | 0.5 | 1.0 | 21.3 |
| Keldon Johnson (SAS) | 99% | 28.1<br><sub>25,29,15,27,23</sub> | 15.1<br><sub>18,11,4,10,10</sub> |  | 6.0<br><sub>4,10,2,5,4</sub> |  | 3.0<br><sub>4,2,1,3,4</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.4 | 24.0 |
| Harrison Barnes (SAS) | 93% | 26.2<br><sub>21,14,10,16,21</sub> | 10.8<br><sub>11,0,0,9,3</sub> |  | 3.1<br><sub>1,0,3,2,5</sub> |  | 1.9<br><sub>1,2,4,1,2</sub> |  | 1.6<br><sub>3,0,0,1,0</sub> |  | 0.7 | 0.2 | 0.9 | 15.9 |
| Carter Bryant (SAS) | 96% | 25.5<br><sub>19,5,2,13,20</sub> | 10.7<br><sub>8,0,0,3,8</sub> |  | 3.9<br><sub>3,1,0,1,3</sub> |  | 1.8<br><sub>2,0,0,0,0</sub> |  | 1.8<br><sub>2,0,0,1,2</sub> |  | 0.6 | 0.6 | 1.0 | 16.4 |
| Jordan McLaughlin (SAS) | 100% | 25.2<br><sub>14,19,-,11,18</sub> | 8.6<br><sub>4,10,-,0,0</sub> |  | 3.6<br><sub>6,1,-,1,3</sub> |  | 4.9<br><sub>2,2,-,5,2</sub> |  | 1.1<br><sub>0,2,-,0,0</sub> |  | 1.9 | 0.2 | 1.2 | 17.1 |
| Luke Kornet (SAS) | 99% | 19.1<br><sub>16,13,14,15,10</sub> | 5.3<br><sub>6,2,2,4,0</sub> |  | 5.5<br><sub>7,2,1,0,3</sub> |  | 1.8<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.7 | 12.6 |
| Tarris Reed Jr. (SAS) | 58% | 16.3<br><sub>11,-,-,-,6</sub> | 5.9<br><sub>2,-,-,-,0</sub> |  | 6.4<br><sub>4,-,-,-,4</sub> |  | 1.0<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.5 | 1.0 | 13.3 |
| David Jones Garcia (SAS) | 58% | 14.9<br><sub>-,-,-,-,4</sub> | 6.1<br><sub>-,-,-,-,0</sub> |  | 2.5<br><sub>-,-,-,-,1</sub> |  | 2.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 10.8 |
| Ja'Kobi Gillespie (SAS) | 88% | 12.3<br><sub>-,-,-,-,-</sub> | 9.8<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 11.2 |
| Maliq Brown (SAS) | 80% | 12.2<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 4.8 |

</details>

<details><summary>if Victor Wembanyama plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. (SAC) | 98% | 36.1<br><sub>35,33,35,36,40</sub> | 23.8<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 3.6 | 35.3 |
| De'Andre Hunter (SAC) | 88% | 32.9<br><sub>42,-,35,37,41</sub> | 13.4<br><sub>24,-,7,30,20</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,-,1,6,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 19.8 |
| Keegan Murray (SAC) | 98% | 31.4<br><sub>40,21,31,40,40</sub> | 11.7<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.9 | 0.9 | 18.3 |
| Zach LaVine (SAC) | 88% | 31.3<br><sub>36,-,32,39,30</sub> | 16.9<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.2 | 2.0 | 23.0 |
| Domantas Sabonis (SAC) | 99% | 30.8<br><sub>35,29,24,38,32</sub> | 14.4<br><sub>21,11,8,19,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 11.6<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 23% · u 77%</sub> | 0.7 | 0.2 | 2.3 | 31.0 |
| Precious Achiuwa (SAC) | 98% | 21.2<br><sub>-,-,8,-,22</sub> | 9.0<br><sub>-,-,0,-,5</sub> |  | 5.6<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.7 |
| Malik Monk (SAC) | 98% | 14.9<br><sub>18,29,20,12,10</sub> | 7.7<br><sub>7,14,8,2,3</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 2.8<br><sub>3,10,2,3,1</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.3 | 1.1 | 11.9 |
| Emanuel Sharp (SAC) | 98% | 14.2<br><sub>7,21,14,10,16</sub> | 4.6<br><sub>4,9,6,3,3</sub> |  | 1.2<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.5 |
| Leaky Black (SAC) | 91% | 13.3<br><sub>12,29,17,19,4</sub> | 2.9<br><sub>0,12,3,0,2</sub> |  | 2.1<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.6 | 0.3 | 0.3 | 5.8 |
| Dylan Cardwell (SAC) | 98% | 12.0<br><sub>13,19,12,10,6</sub> | 3.7<br><sub>6,10,6,0,0</sub> |  | 4.1<br><sub>3,6,4,4,1</sub> |  | 0.9<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 8.7 |
| Alex Karaban (SAC) | 48% | 8.0<br><sub>-,29,4,-,-</sub> | 1.6<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |
| Daeqwon Plowden (SAC) | 58% | 8.0<br><sub>2,24,4,-,-</sub> | 2.9<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Mason Plumlee (SAC) | 48% | 6.1<br><sub>-,5,4,-,-</sub> | 1.9<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.5 |
| Devin Vassell (SAS) | 99% | 33.1<br><sub>23,32,36,32,26</sub> | 15.6<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>2,6,5,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.7<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.5 | 1.1 | 23.8 |
| Stephon Castle (SAS) | 99% | 32.6<br><sub>25,35,31,33,29</sub> | 20.6<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 8.0<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>5,0,2,2,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.0 | 33.8 |
| Victor Wembanyama (SAS) | 100% | 32.3<br><sub>21,35,34,33,32</sub> | 31.7<br><sub>12,26,25,32,50</sub> | 29.5 · – | 12.2<br><sub>12,10,18,11,19</sub> | 11.5 | 4.6<br><sub>6,6,4,3,1</sub> | 3.5 | 2.4<br><sub>0,4,1,2,5</sub> | 2.5 | 1.2 | 3.3 | 2.7 | 48.4 |
| Julian Champagnie (SAS) | 99% | 29.3<br><sub>23,24,30,29,25</sub> | 12.1<br><sub>7,4,14,20,9</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>8,5,6,4,3</sub> |  | 2.0<br><sub>3,1,0,1,3</sub> |  | 2.2<br><sub>1,1,4,4,3</sub> |  | 1.1 | 0.5 | 0.8 | 18.8 |
| Keldon Johnson (SAS) | 99% | 27.2<br><sub>25,29,15,27,23</sub> | 12.6<br><sub>18,11,4,10,10</sub> |  | 5.7<br><sub>4,10,2,5,4</sub> |  | 2.6<br><sub>4,2,1,3,4</sub> |  | 0.9<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.2 | 20.8 |
| Harrison Barnes (SAS) | 93% | 22.1<br><sub>21,14,10,16,21</sub> | 8.0<br><sub>11,0,0,9,3</sub> |  | 2.5<br><sub>1,0,3,2,5</sub> |  | 1.5<br><sub>1,2,4,1,2</sub> |  | 1.1<br><sub>3,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 12.0 |
| Carter Bryant (SAS) | 96% | 19.2<br><sub>19,5,2,13,20</sub> | 7.0<br><sub>8,0,0,3,8</sub> |  | 2.9<br><sub>3,1,0,1,3</sub> |  | 1.3<br><sub>2,0,0,0,0</sub> |  | 1.1<br><sub>2,0,0,1,2</sub> |  | 0.4 | 0.4 | 0.7 | 11.2 |
| Luke Kornet (SAS) | 99% | 18.3<br><sub>16,13,14,15,10</sub> | 4.4<br><sub>6,2,2,4,0</sub> |  | 5.1<br><sub>7,2,1,0,3</sub> |  | 1.6<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.6 | 11.1 |
| Tarris Reed Jr. (SAS) | 58% | 12.7<br><sub>11,-,-,-,6</sub> | 3.9<br><sub>2,-,-,-,0</sub> |  | 5.1<br><sub>4,-,-,-,4</sub> |  | 0.7<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.7 | 9.8 |
| David Jones Garcia (SAS) | 58% | 10.9<br><sub>-,-,-,-,4</sub> | 4.0<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.2 | 0.6 | 7.4 |
| Ja'Kobi Gillespie (SAS) | 88% | 10.0<br><sub>-,-,-,-,-</sub> | 5.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.7 |
| Maliq Brown (SAS) | 80% | 9.4<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 3.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-23/`._
