# NBA model · Thu 29 Oct 2026 (US date)

Updated **Fri 30 Oct, 02:36 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

_No bets clear the edge threshold right now._

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jrue Holiday 15+ pra **+** Deni Avdija 5+ reb | MEM @ POR | 61.3% | 1.63 | 1.71 | 1.51 | -7.4% |
| NOP win **+** Domantas Sabonis 20+ pra | SAC @ NOP | 60.4% | 1.66 | 1.74 | 1.53 | -7.4% |
| Deni Avdija 5+ reb **+** Donovan Clingan 6+ pts | MEM @ POR | 60.2% | 1.66 | 1.74 | 1.51 | -9.0% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker reb under 3.5 **+** Donovan Mitchell 20+ pra | CLE @ ATL | 52.1% | 1.92 | 2.01 | 1.83 | -4.8% |
| Nickeil Alexander-Walker reb under 3.5 **+** Donovan Mitchell 1+ 3pm | CLE @ ATL | 51.9% | 1.93 | 2.02 | 1.83 | -4.9% |
| NOP win **+** Precious Achiuwa 6+ pts | SAC @ NOP | 55.7% | 1.80 | 1.89 | 1.67 | -7.0% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jalen Johnson pra under 39.5 **+** Donovan Mitchell 20+ pra | CLE @ ATL | 48.8% | 2.05 | 2.15 | 2.03 | -1.0% |
| Jalen Johnson pra under 39.5 **+** Donovan Mitchell 1+ 3pm | CLE @ ATL | 48.5% | 2.06 | 2.16 | 2.04 | -1.1% |
| Jalen Johnson ra under 17.5 **+** Donovan Mitchell 1+ 3pm | CLE @ ATL | 50.8% | 1.97 | 2.07 | 1.94 | -1.5% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Ty Jerome pr under 27.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 41.8% | 2.39 | 2.51 | 2.44 | +2.1% |
| Ty Jerome pra under 33.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 41.5% | 2.41 | 2.53 | 2.46 | +2.0% |
| Ty Jerome pa under 30.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 42.7% | 2.34 | 2.46 | 2.37 | +1.4% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PTS over 14.5 | SAC @ NOP | draftkings | 3.64 | 2.40 | 41.6% | 25.7% | 29.7% | +8.0% | +51.5% | 0.8% |
| Jrue Holiday REB over 4.5 | MEM @ POR | draftkings | 2.99 | 2.07 | 48.3% | 31.3% | 35.5% | +6.2% | +44.5% | 0.8% |
| Ty Jerome PR under 27.5 | MEM @ POR | draftkings | 1.92 | 1.34 | 74.9% | 48.7% | 55.3% | +6.0% | +43.5% | 1.6% |
| Ty Jerome PRA under 33.5 | MEM @ POR | draftkings | 1.93 | 1.34 | 74.5% | 48.5% | 55.0% | +5.9% | +43.4% | 1.6% |
| Jrue Holiday AST over 4.5 | MEM @ POR | draftkings | 2.49 | 1.74 | 57.4% | 37.5% | 42.5% | +5.8% | +43.0% | 1.0% |
| Jalen Johnson PRA under 39.5 | CLE @ ATL | draftkings | 1.90 | 1.34 | 74.7% | 49.2% | 55.6% | +5.6% | +42.0% | 1.6% |
| Ty Jerome PA under 30.5 | MEM @ POR | draftkings | 1.86 | 1.32 | 75.8% | 50.2% | 56.6% | +5.4% | +41.1% | 1.6% |
| Ty Jerome PTS under 24.5 | MEM @ POR | draftkings | 1.84 | 1.31 | 76.2% | 50.8% | 57.1% | +5.1% | +40.2% | 1.5% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CLE @ ATL | Fri 30 Oct 11:00 | 117.6–117.5 | CLE 50% | 2.00 / 2.00 | ATL +0.5 | 234.5 | ATL -1.5 covers 47%; o237.5 45% |
| SAC @ NOP | Fri 30 Oct 11:00 | 115.6–122.8 | SAC 30% | 3.30 / 1.43 | NOP -7.5 | 238.5 | NOP -5.5 covers 55%; o236.5 54% |
| MEM @ POR | Fri 30 Oct 13:00 | 110.2–119.5 | MEM 25% | 3.93 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o232.5 44% |

### CLE @ ATL
Out: Mouhamed Gueye (ATL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker PA under 21.5 | CLE @ ATL | draftkings | 1.88 | 1.56 | 64.2% | 49.6% | 53.2% | +0.3% | +20.9% | 0.1% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker reb under 3.5 **+** Donovan Mitchell 20+ pra | 52.1% | 1.92 | 2.01 | 1.83 | -4.8% |
| Jalen Johnson pra under 39.5 **+** Donovan Mitchell 20+ pra | 48.8% | 2.05 | 2.15 | 2.03 | -1.0% |
| Jalen Johnson pra under 39.5 **+** Donovan Mitchell 3+ reb | 44.4% | 2.25 | 2.37 | 2.23 | -1.0% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.1 | 17.9 | 4.5 | 6.3 | 2.2 | 1.3 | 0.5 | 3.7 | 28.6 |
| Donovan Mitchell | 98% | 35.1 | 25.7 | 5.0 | 4.4 | 2.8 | 1.4 | 0.4 | 2.9 | 35.1 |
| Evan Mobley | 98% | 33.6 | 17.9 | 8.9 | 3.3 | 1.2 | 1.0 | 1.6 | 2.0 | 30.1 |
| Peyton Watson | 98% | 30.4 | 14.2 | 4.5 | 2.1 | 1.3 | 1.0 | 1.1 | 2.1 | 20.7 |
| Jarrett Allen | 98% | 27.7 | 13.2 | 8.3 | 1.4 | 0.1 | 0.9 | 1.4 | 1.4 | 23.0 |
| Sam Merrill | 98% | 21.4 | 7.7 | 2.0 | 1.5 | 1.3 | 0.6 | 0.1 | 0.6 | 11.1 |
| Jaylon Tyson | 96% | 18.4 | 7.4 | 3.3 | 1.7 | 0.8 | 0.5 | 0.3 | 1.0 | 12.4 |
| Meleek Thomas | 63% | 18.0 | 7.8 | 2.6 | 0.9 | 0.8 | 0.7 | 0.1 | 1.1 | 11.3 |
| Mario Hezonja | 93% | 14.6 | 5.7 | 3.0 | 0.9 | 0.6 | 0.4 | 0.2 | 0.7 | 9.5 |
| Craig Porter Jr. | 52% | 8.1 | 2.2 | 1.5 | 1.2 | 0.1 | 0.4 | 0.2 | 0.6 | 4.9 |
| Tyrese Proctor | 64% | 7.8 | 3.7 | 1.0 | 1.1 | 0.3 | 0.4 | 0.0 | 0.6 | 5.8 |
| Thomas Bryant | 30% | 7.7 | 3.7 | 2.1 | 0.4 | 0.3 | 0.2 | 0.2 | 0.4 | 6.2 |
| Riley Minix | 23% | 6.5 | 2.7 | 0.9 | 0.4 | 0.2 | 0.2 | 0.1 | 0.3 | 4.0 |
| Tristan Enaruna | 23% | 5.4 | 2.1 | 0.9 | 0.4 | 0.1 | 0.2 | 0.1 | 0.2 | 3.4 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 31.0 | 19.0 | 8.0 | 6.3 | 1.5 | 1.1 | 0.5 | 2.6 | 33.2 |
| Nickeil Alexander-Walker | 98% | 28.1 | 16.8 | 2.6 | 2.8 | 2.6 | 1.0 | 0.4 | 1.8 | 22.2 |
| Dyson Daniels | 98% | 26.1 | 9.8 | 5.2 | 4.2 | 0.5 | 1.9 | 0.3 | 1.4 | 19.2 |
| Onyeka Okongwu | 98% | 25.8 | 11.4 | 5.8 | 2.2 | 1.3 | 1.0 | 0.7 | 1.1 | 19.4 |
| CJ McCollum | 98% | 24.9 | 15.7 | 2.4 | 2.6 | 1.9 | 0.8 | 0.5 | 1.6 | 20.6 |
| Aaron Wiggins | 91% | 20.6 | 9.5 | 2.6 | 1.4 | 1.3 | 0.8 | 0.2 | 0.8 | 13.4 |
| Luguentz Dort | 98% | 19.3 | 7.1 | 2.4 | 1.1 | 0.9 | 0.7 | 0.2 | 0.6 | 10.6 |
| Kingston Flemings | 96% | 17.8 | 6.9 | 2.8 | 3.3 | 0.6 | 0.6 | 0.2 | 1.4 | 13.0 |
| Jock Landale | 98% | 16.8 | 8.0 | 4.0 | 1.4 | 0.6 | 0.5 | 0.4 | 0.8 | 13.4 |
| Jalen Wilson | 76% | 7.9 | 3.5 | 1.3 | 0.6 | 0.3 | 0.3 | 0.1 | 0.4 | 5.4 |
| Corey Kispert | 52% | 7.7 | 4.6 | 1.0 | 0.6 | 0.5 | 0.1 | 0.1 | 0.3 | 6.2 |
| Asa Newell | 52% | 6.8 | 3.2 | 1.4 | 0.4 | 0.2 | 0.2 | 0.2 | 0.3 | 5.0 |
| Dorian Finney-Smith | 52% | 6.7 | 2.1 | 1.1 | 0.4 | 0.1 | 0.2 | 0.1 | 0.3 | 3.6 |
| Keshon Gilbert | 88% | 6.3 | 1.9 | 0.8 | 0.8 | 0.1 | 0.3 | 0.2 | 0.5 | 3.6 |
| RayJ Dennis | 63% | 6.1 | 2.4 | 0.8 | 0.9 | 0.2 | 0.2 | 0.1 | 0.4 | 4.1 |
| Zuby Ejiofor | 52% | 5.7 | 2.5 | 1.0 | 0.5 | 0.1 | 0.2 | 0.1 | 0.3 | 4.0 |

</details>


### SAC @ NOP
Out: Yves Missi (NOP), Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PR over 18.5 | SAC @ NOP | draftkings | 1.85 | 1.52 | 65.7% | 50.8% | 54.5% | +0.7% | +21.4% | 0.2% |
| Darius Acuff Jr. PA under 27.5 | SAC @ NOP | draftkings | 1.93 | 1.58 | 63.3% | 48.5% | 52.2% | +0.6% | +22.0% | 0.2% |
| Domantas Sabonis AST under 6.5 | SAC @ NOP | draftkings | 1.93 | 1.59 | 62.8% | 48.5% | 52.1% | +0.3% | +21.0% | 0.1% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| NOP win **+** Domantas Sabonis 20+ pra | 60.4% | 1.66 | 1.74 | 1.53 | -7.4% |
| NOP win **+** Precious Achiuwa 6+ pts | 55.7% | 1.80 | 1.89 | 1.67 | -7.0% |
| Precious Achiuwa 19+ pr **+** Domantas Sabonis 25+ pra | 46.8% | 2.14 | 2.24 | 2.03 | -5.1% |
| Precious Achiuwa 11+ pts **+** Domantas Sabonis 25+ pra | 46.4% | 2.16 | 2.26 | 2.10 | -2.5% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.6–122.8 | SAC 30% | 3.30 / 1.43 | NOP -7.5 | 238.5 | NOP -5.5 covers 55%; o236.5 54% |
| Expected (weighted by chance each plays) | 115.3–123.6 | SAC 28% | 3.59 / 1.39 | NOP -8.5 | 239.5 | NOP -5.5 covers 58%; o236.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Poole (NOP) | Day-To-Day | 70% | 15.3 | 7.5 | 1.6 | 2.0 | 1.1 | 0.6 | 0.3 | 0.9 | 11.1 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 93% | 34.8 | 20.9 | 3.9 | 4.7 | 2.1 | 1.1 | 0.5 | 2.8 | 29.5 |
| Domantas Sabonis | 98% | 34.5 | 18.9 | 14.5 | 5.9 | 0.4 | 0.9 | 0.4 | 2.6 | 39.2 |
| Zach LaVine | 98% | 34.3 | 21.9 | 3.4 | 2.9 | 2.8 | 0.9 | 0.3 | 2.3 | 28.2 |
| Precious Achiuwa | 98% | 29.7 | 14.0 | 8.3 | 1.7 | 0.4 | 1.1 | 1.0 | 1.3 | 24.0 |
| De'Andre Hunter | 98% | 27.8 | 11.7 | 5.2 | 1.6 | 1.7 | 0.8 | 0.2 | 1.2 | 18.5 |
| Daeqwon Plowden | 98% | 18.2 | 6.0 | 2.1 | 0.9 | 0.9 | 0.5 | 0.2 | 0.6 | 8.9 |
| Jonathan Mogbo | 64% | 16.1 | 5.6 | 2.9 | 0.9 | 0.5 | 0.5 | 0.3 | 0.7 | 9.4 |
| Malik Monk | 96% | 15.6 | 8.1 | 1.6 | 2.7 | 1.0 | 0.5 | 0.3 | 1.1 | 12.4 |
| Emanuel Sharp | 93% | 15.3 | 5.0 | 1.0 | 1.0 | 0.6 | 0.5 | 0.2 | 0.6 | 6.9 |
| Nique Clifford | 72% | 12.4 | 4.8 | 1.9 | 1.2 | 0.4 | 0.5 | 0.2 | 0.9 | 8.0 |
| Leaky Black | 52% | 11.2 | 3.1 | 2.1 | 0.8 | 0.3 | 0.5 | 0.3 | 0.4 | 6.0 |
| Alex Karaban | 58% | 9.3 | 2.5 | 1.8 | 0.6 | 0.0 | 0.3 | 0.2 | 0.5 | 4.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 34.4 | 18.6 | 5.2 | 3.4 | 3.2 | 1.4 | 0.5 | 1.6 | 27.2 |
| Dejounte Murray | 98% | 32.5 | 18.8 | 5.9 | 6.9 | 1.6 | 1.9 | 0.4 | 3.0 | 31.5 |
| Zion Williamson | 96% | 32.3 | 21.2 | 5.6 | 3.4 | 0.2 | 1.3 | 0.7 | 2.1 | 30.1 |
| Saddiq Bey | 96% | 28.6 | 15.9 | 4.7 | 2.2 | 2.1 | 0.9 | 0.2 | 1.0 | 22.8 |
| Jeremiah Fears | 98% | 26.5 | 14.6 | 3.7 | 3.4 | 1.4 | 1.2 | 0.4 | 2.1 | 21.7 |
| Derik Queen | 98% | 26.3 | 12.5 | 8.1 | 3.0 | 0.3 | 1.1 | 1.0 | 2.1 | 23.7 |
| Herbert Jones | 96% | 19.7 | 5.9 | 2.3 | 1.6 | 0.8 | 1.1 | 0.4 | 0.8 | 9.8 |
| Bennedict Mathurin | 98% | 18.3 | 8.7 | 3.4 | 1.6 | 0.6 | 0.5 | 0.2 | 1.2 | 13.7 |
| Karlo Matkovic | 86% | 15.5 | 5.8 | 3.9 | 0.9 | 0.5 | 0.5 | 1.0 | 0.6 | 10.5 |
| DeAndre Jordan | 58% | 15.1 | 4.2 | 6.0 | 0.8 | 0.0 | 0.4 | 0.7 | 0.7 | 11.1 |
| AJ Johnson | 8% | 12.7 | 5.2 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.5 |
| Trendon Watford | 26% | 10.4 | 3.8 | 1.9 | 1.2 | 0.1 | 0.3 | 0.3 | 0.7 | 6.9 |
| Bryce McGowens | 52% | 9.9 | 3.4 | 1.2 | 0.6 | 0.2 | 0.4 | 0.1 | 0.3 | 5.2 |
| Malik Dia | 35% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 5.9 |
| Jaron Pierre Jr. | 40% | 8.6 | 3.5 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.8 |
| Julian Reese | 30% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 5.9 |

</details>


### MEM @ POR
Out: Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3PM under 2.5 | MEM @ POR | draftkings | 2.24 | 1.76 | 56.7% | 41.7% | 45.5% | +1.9% | +27.1% | 0.4% |
| Damian Lillard PRA under 28.5 | MEM @ POR | draftkings | 1.94 | 1.60 | 62.4% | 48.1% | 51.7% | +0.4% | +21.3% | 0.1% |
| Jrue Holiday PRA over 19.5 | MEM @ POR | draftkings | 1.78 | 1.49 | 67.3% | 52.5% | 56.2% | +0.1% | +19.9% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Jrue Holiday 15+ pra **+** Deni Avdija 5+ reb | 61.3% | 1.63 | 1.71 | 1.51 | -7.4% |
| Jrue Holiday 15+ pra **+** Deni Avdija 5+ reb **+** Donovan Clingan 6+ pts | 48.0% | 2.08 | 2.19 | 1.84 | -11.6% |
| Cedric Coward pr under 19.5 **+** Jrue Holiday 1+ 3pm | 46.5% | 2.15 | 2.26 | 2.10 | -2.3% |
| Ty Jerome pr under 27.5 **+** Jrue Holiday 3+ ast | 41.8% | 2.39 | 2.51 | 2.44 | +2.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.2–119.5 | MEM 25% | 3.93 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o232.5 44% |
| Expected (weighted by chance each plays) | 110.2–119.9 | MEM 24% | 4.19 / 1.31 | POR -9.5 | 230.5 | POR -7.5 covers 56%; o232.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| John Tonje (POR) | Questionable | 55% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |
| Jayson Kent (POR) | Questionable | 55% | 5.6 | 2.2 | 1.0 | 0.4 | 0.2 | 0.3 | 0.1 | 0.4 | 3.5 | small |
| Chris Youngblood (POR) | Questionable | 55% | 5.5 | 2.3 | 0.9 | 0.4 | 0.2 | 0.2 | 0.1 | 0.3 | 3.6 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 93% | 29.5 | 12.7 | 8.4 | 3.9 | 1.2 | 1.0 | 0.7 | 2.2 | 25.0 |
| Ty Jerome | 98% | 26.7 | 19.1 | 3.0 | 5.4 | 1.9 | 1.1 | 0.3 | 2.4 | 27.6 |
| Cedric Coward | 98% | 25.2 | 10.2 | 5.7 | 2.3 | 1.1 | 0.9 | 0.5 | 1.8 | 18.2 |
| Jaylen Wells | 98% | 24.6 | 9.7 | 2.8 | 1.3 | 1.2 | 1.1 | 0.1 | 1.0 | 13.8 |
| Jerami Grant | 98% | 21.7 | 9.8 | 2.3 | 1.5 | 1.0 | 0.8 | 0.7 | 1.4 | 13.6 |
| Zach Edey | 98% | 20.4 | 8.2 | 7.7 | 1.0 | 0.1 | 0.6 | 1.4 | 1.5 | 16.9 |
| Cam Spencer | 96% | 16.4 | 6.6 | 1.8 | 3.4 | 0.8 | 0.7 | 0.1 | 0.9 | 11.8 |
| Scotty Pippen Jr. | 97% | 15.0 | 7.4 | 2.1 | 2.7 | 0.6 | 1.2 | 0.3 | 1.5 | 12.2 |
| GG Jackson | 96% | 14.1 | 7.9 | 2.7 | 0.9 | 0.6 | 0.5 | 0.6 | 1.1 | 11.5 |
| Isaiah Stewart | 98% | 13.1 | 5.0 | 2.9 | 0.6 | 0.3 | 0.3 | 0.8 | 0.7 | 8.5 |
| Karim Lopez | 23% | 12.5 | 5.5 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.8 |
| Olivier-Maxence Prosper | 30% | 11.6 | 5.8 | 2.3 | 0.6 | 0.4 | 0.6 | 0.2 | 0.7 | 8.7 |
| Quinten Post | 88% | 11.4 | 3.7 | 2.1 | 0.6 | 0.3 | 0.3 | 0.3 | 0.6 | 6.3 |
| Javon Small | 86% | 9.7 | 4.2 | 1.5 | 1.4 | 0.4 | 0.5 | 0.1 | 0.8 | 7.2 |
| Carson Cooper | 35% | 8.6 | 3.7 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Kris Murray | 48% | 8.3 | 1.9 | 1.4 | 0.6 | 0.1 | 0.4 | 0.2 | 0.4 | 3.9 |
| Jahmai Mashack | 38% | 8.2 | 2.5 | 1.1 | 0.9 | 0.1 | 0.5 | 0.2 | 0.7 | 4.5 |
| Taylor Hendricks | 52% | 7.2 | 2.8 | 1.4 | 0.3 | 0.2 | 0.4 | 0.2 | 0.3 | 4.5 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 97% | 33.5 | 23.4 | 7.7 | 6.5 | 1.8 | 0.9 | 0.7 | 3.7 | 37.6 |
| Damian Lillard | 98% | 31.0 | 17.1 | 4.5 | 5.1 | 2.5 | 1.2 | 0.2 | 2.3 | 26.8 |
| Jrue Holiday | 98% | 29.1 | 14.1 | 4.8 | 5.2 | 2.2 | 1.1 | 0.2 | 2.2 | 24.0 |
| Ja Morant | 98% | 28.9 | 18.1 | 3.8 | 7.2 | 1.4 | 1.2 | 0.3 | 2.9 | 29.1 |
| Toumani Camara | 98% | 28.8 | 12.1 | 4.5 | 1.9 | 2.0 | 1.2 | 0.4 | 1.3 | 18.4 |
| Donovan Clingan | 98% | 23.9 | 10.5 | 10.6 | 1.9 | 1.1 | 0.6 | 1.9 | 1.2 | 23.0 |
| Sidy Cissoko | 93% | 19.7 | 5.7 | 2.8 | 1.7 | 0.6 | 1.0 | 0.4 | 1.0 | 10.3 |
| Scoot Henderson | 98% | 19.3 | 9.7 | 2.0 | 2.6 | 1.2 | 0.9 | 0.2 | 1.8 | 14.3 |
| Robert Williams III | 98% | 18.4 | 7.7 | 8.0 | 1.1 | 0.2 | 0.6 | 1.5 | 1.0 | 16.9 |
| Micah Potter | 52% | 11.6 | 5.1 | 3.4 | 0.7 | 0.5 | 0.3 | 0.2 | 0.7 | 9.2 |
| Vit Krejci | 96% | 9.1 | 3.5 | 1.3 | 0.8 | 0.4 | 0.4 | 0.1 | 0.3 | 5.7 |
| Branden Carlson | 16% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Yang Hansen | 52% | 6.1 | 2.2 | 1.6 | 0.4 | 0.1 | 0.1 | 0.2 | 0.6 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-29/`._
