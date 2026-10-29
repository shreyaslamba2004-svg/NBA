# NBA model · Thu 29 Oct 2026 (US date)

Updated **Fri 30 Oct, 01:06 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PTS over 14.5 | SAC @ NOP | draftkings | 3.55 | 2.44 | 40.9% | 26.3% | 30.0% | +6.4% | +45.3% | 0.6% |

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| NOP win **+** Domantas Sabonis 20+ pra | SAC @ NOP | 60.3% | 1.66 | 1.74 | 1.54 | -7.4% |
| NOP win **+** Domantas Sabonis 8+ reb | SAC @ NOP | 58.1% | 1.72 | 1.81 | 1.59 | -7.4% |
| Deni Avdija 5+ reb **+** Donovan Clingan 6+ pts | MEM @ POR | 59.3% | 1.69 | 1.77 | 1.53 | -9.6% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| NOP win **+** Jeremiah Fears 8+ pts | SAC @ NOP | 51.1% | 1.96 | 2.06 | 1.85 | -5.8% |
| Nickeil Alexander-Walker reb under 3.5 **+** Donovan Mitchell 1+ 3pm | CLE @ ATL | 52.0% | 1.92 | 2.02 | 1.81 | -6.0% |
| Nickeil Alexander-Walker reb under 3.5 **+** Peyton Watson 6+ pts | CLE @ ATL | 52.9% | 1.89 | 1.98 | 1.78 | -6.0% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Ty Jerome pa under 30.5 **+** Toumani Camara 6+ pts | MEM @ POR | 47.7% | 2.09 | 2.20 | 2.10 | +0.2% |
| Ty Jerome pra under 34.5 **+** Jrue Holiday 1+ 3pm | MEM @ POR | 48.5% | 2.06 | 2.17 | 2.06 | +0.1% |
| Ty Jerome pra under 34.5 **+** Toumani Camara 6+ pts | MEM @ POR | 48.7% | 2.05 | 2.16 | 2.05 | -0.1% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Cedric Coward pts under 12.5 **+** Jrue Holiday 15+ pra | MEM @ POR | 42.3% | 2.36 | 2.48 | 2.43 | +2.7% |
| Ty Jerome pa under 30.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 43.0% | 2.33 | 2.44 | 2.39 | +2.6% |
| Ty Jerome pr under 27.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 42.3% | 2.37 | 2.48 | 2.43 | +2.6% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 5.5 | MEM @ POR | draftkings | 3.98 | 2.26 | 44.2% | 23.5% | 28.7% | +14.1% | +76.1% | 1.2% |
| Jrue Holiday PRA over 24.5 | MEM @ POR | draftkings | 3.38 | 2.28 | 43.8% | 27.7% | 31.7% | +7.1% | +48.1% | 0.8% |
| Jrue Holiday AST over 4.5 | MEM @ POR | draftkings | 2.50 | 1.69 | 59.2% | 37.4% | 42.8% | +7.1% | +48.1% | 1.2% |
| Cedric Coward PTS under 12.5 | MEM @ POR | draftkings | 1.97 | 1.34 | 74.6% | 47.4% | 54.2% | +6.9% | +47.0% | 1.8% |
| Ty Jerome PR under 27.5 | MEM @ POR | draftkings | 1.88 | 1.30 | 77.1% | 49.6% | 56.5% | +6.5% | +45.4% | 1.8% |
| Ty Jerome PA under 30.5 | MEM @ POR | draftkings | 1.85 | 1.28 | 78.2% | 50.4% | 57.3% | +6.3% | +45.0% | 1.8% |
| Ty Jerome PRA under 34.5 | MEM @ POR | draftkings | 1.81 | 1.26 | 79.5% | 51.5% | 58.6% | +6.2% | +44.2% | 1.9% |
| Jrue Holiday REB over 4.5 | MEM @ POR | draftkings | 3.06 | 2.12 | 47.1% | 30.5% | 34.7% | +6.1% | +44.1% | 0.7% |
| Ty Jerome PTS under 24.5 | MEM @ POR | draftkings | 1.83 | 1.28 | 78.2% | 51.2% | 57.9% | +5.8% | +42.8% | 1.8% |
| Jrue Holiday RA over 7.5 | MEM @ POR | draftkings | 1.97 | 1.39 | 71.9% | 47.5% | 53.6% | +5.6% | +41.7% | 1.4% |
| Cedric Coward PR under 19.5 | MEM @ POR | draftkings | 1.83 | 1.30 | 76.9% | 51.0% | 57.5% | +5.3% | +40.9% | 1.6% |
| Cameron Boozer PTS under 15.5 | MEM @ POR | draftkings | 1.98 | 1.41 | 71.0% | 47.2% | 53.1% | +5.2% | +40.6% | 1.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CLE @ ATL | Fri 30 Oct 11:00 | 117.6–117.5 | CLE 50% | 2.00 / 2.00 | ATL +0.5 | 234.5 | ATL -1.5 covers 47%; o237.5 45% |
| SAC @ NOP | Fri 30 Oct 11:00 | 115.6–122.8 | SAC 30% | 3.30 / 1.43 | NOP -7.5 | 238.5 | NOP -6.5 covers 52%; o236.5 54% |
| MEM @ POR | Fri 30 Oct 13:00 | 110.2–119.5 | MEM 25% | 3.93 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o233.5 42% |

### CLE @ ATL
Out: Mouhamed Gueye (ATL)

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| James Harden 3+ reb **+** Donovan Mitchell 1+ 3pm **+** Peyton Watson 8+ pts | 56.5% | 1.77 | 1.86 | 1.52 | -14.0% |
| Nickeil Alexander-Walker reb under 3.5 **+** Donovan Mitchell 1+ 3pm | 52.0% | 1.92 | 2.02 | 1.81 | -6.0% |
| Jalen Johnson pr under 31.5 **+** Peyton Watson 6+ pts | 48.0% | 2.08 | 2.19 | 2.05 | -1.6% |
| Jalen Johnson pr under 31.5 **+** James Harden 3+ reb | 41.5% | 2.41 | 2.53 | 2.37 | -1.8% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 37.2 | 18.9 | 4.8 | 6.7 | 2.3 | 1.4 | 0.5 | 4.0 | 30.4 |
| Donovan Mitchell | 98% | 37.0 | 26.6 | 5.2 | 4.5 | 3.0 | 1.5 | 0.4 | 3.1 | 36.3 |
| Evan Mobley | 98% | 35.7 | 18.5 | 9.5 | 3.4 | 1.4 | 1.0 | 1.7 | 2.2 | 31.4 |
| Peyton Watson | 98% | 32.3 | 14.6 | 4.8 | 2.2 | 1.3 | 1.1 | 1.3 | 2.1 | 21.6 |
| Jarrett Allen | 98% | 29.5 | 13.7 | 8.9 | 1.6 | 0.1 | 1.0 | 1.4 | 1.5 | 24.2 |
| Sam Merrill | 98% | 22.2 | 7.3 | 2.1 | 1.6 | 1.2 | 0.6 | 0.1 | 0.7 | 10.9 |
| Jaylon Tyson | 96% | 19.2 | 7.3 | 3.3 | 1.8 | 0.8 | 0.5 | 0.3 | 1.1 | 12.4 |
| Meleek Thomas | 63% | 18.5 | 7.4 | 2.6 | 0.9 | 0.8 | 0.7 | 0.1 | 1.1 | 10.8 |
| Mario Hezonja | 93% | 15.1 | 5.2 | 2.8 | 0.9 | 0.5 | 0.5 | 0.2 | 0.8 | 8.9 |
| Tyrese Proctor | 64% | 8.8 | 4.0 | 1.1 | 1.2 | 0.4 | 0.4 | 0.1 | 0.7 | 6.3 |
| Craig Porter Jr. | 52% | 8.7 | 2.2 | 1.6 | 1.4 | 0.1 | 0.4 | 0.3 | 0.7 | 5.2 |
| Riley Minix | 23% | 7.9 | 2.9 | 1.0 | 0.5 | 0.2 | 0.2 | 0.1 | 0.4 | 4.4 |
| Thomas Bryant | 30% | 7.7 | 3.4 | 2.2 | 0.4 | 0.3 | 0.2 | 0.3 | 0.4 | 5.9 |
| Tristan Enaruna | 23% | 6.6 | 2.1 | 1.1 | 0.4 | 0.1 | 0.3 | 0.1 | 0.3 | 3.7 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 31.5 | 18.9 | 8.2 | 6.5 | 1.5 | 1.1 | 0.5 | 2.6 | 33.7 |
| Nickeil Alexander-Walker | 98% | 29.0 | 17.8 | 2.7 | 2.9 | 2.7 | 1.1 | 0.4 | 1.8 | 23.4 |
| Dyson Daniels | 98% | 27.2 | 10.3 | 5.4 | 4.4 | 0.5 | 2.0 | 0.3 | 1.5 | 20.0 |
| Onyeka Okongwu | 98% | 26.9 | 11.9 | 6.1 | 2.4 | 1.4 | 1.0 | 0.9 | 1.2 | 20.4 |
| CJ McCollum | 98% | 25.5 | 16.1 | 2.4 | 2.7 | 2.0 | 0.8 | 0.5 | 1.6 | 21.2 |
| Aaron Wiggins | 91% | 21.3 | 9.2 | 2.6 | 1.5 | 1.2 | 0.8 | 0.2 | 0.9 | 13.2 |
| Luguentz Dort | 98% | 20.3 | 7.5 | 2.5 | 1.3 | 1.1 | 0.8 | 0.2 | 0.7 | 11.2 |
| Kingston Flemings | 96% | 19.1 | 7.3 | 2.9 | 3.5 | 0.6 | 0.6 | 0.3 | 1.4 | 13.6 |
| Jock Landale | 98% | 16.9 | 7.7 | 4.1 | 1.6 | 0.6 | 0.4 | 0.5 | 0.8 | 13.3 |
| Jalen Wilson | 76% | 8.1 | 3.4 | 1.3 | 0.6 | 0.3 | 0.2 | 0.0 | 0.4 | 5.3 |
| Corey Kispert | 52% | 8.0 | 4.4 | 1.1 | 0.7 | 0.5 | 0.1 | 0.1 | 0.3 | 6.2 |
| Asa Newell | 52% | 6.8 | 3.1 | 1.4 | 0.4 | 0.2 | 0.2 | 0.2 | 0.3 | 4.9 |
| Dorian Finney-Smith | 52% | 6.7 | 1.9 | 1.1 | 0.4 | 0.1 | 0.2 | 0.1 | 0.3 | 3.4 |
| Keshon Gilbert | 88% | 6.1 | 1.8 | 0.8 | 0.8 | 0.1 | 0.2 | 0.2 | 0.4 | 3.4 |
| Zuby Ejiofor | 52% | 5.8 | 2.4 | 1.1 | 0.5 | 0.2 | 0.2 | 0.1 | 0.3 | 4.0 |
| RayJ Dennis | 63% | 5.8 | 2.3 | 0.7 | 0.9 | 0.2 | 0.2 | 0.1 | 0.4 | 4.0 |

</details>


### SAC @ NOP
Out: Yves Missi (NOP), Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. PTS under 22.5 | SAC @ NOP | draftkings | 1.89 | 1.57 | 63.5% | 49.4% | 52.9% | +0.1% | +20.2% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| NOP win **+** Domantas Sabonis 20+ pra | 60.3% | 1.66 | 1.74 | 1.54 | -7.4% |
| NOP win **+** Jeremiah Fears 8+ pts | 51.1% | 1.96 | 2.06 | 1.85 | -5.8% |
| Precious Achiuwa 11+ pts **+** Domantas Sabonis 25+ pra | 46.7% | 2.14 | 2.25 | 2.08 | -2.9% |
| Precious Achiuwa 11+ pts **+** Trey Murphy III 2+ 3pm | 40.7% | 2.46 | 2.58 | 2.40 | -2.4% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.6–122.8 | SAC 30% | 3.30 / 1.43 | NOP -7.5 | 238.5 | NOP -6.5 covers 52%; o236.5 54% |
| Expected (weighted by chance each plays) | 115.3–123.6 | SAC 28% | 3.59 / 1.39 | NOP -8.5 | 239.5 | NOP -6.5 covers 55%; o236.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Poole (NOP) | Day-To-Day | 70% | 14.1 | 7.3 | 1.5 | 1.8 | 1.2 | 0.5 | 0.3 | 0.9 | 10.6 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 93% | 34.6 | 20.7 | 3.6 | 4.6 | 2.2 | 1.1 | 0.4 | 2.7 | 28.9 |
| Domantas Sabonis | 98% | 33.9 | 19.1 | 14.4 | 5.7 | 0.3 | 0.9 | 0.4 | 2.6 | 39.2 |
| Zach LaVine | 98% | 33.4 | 20.9 | 3.4 | 2.9 | 2.6 | 0.9 | 0.2 | 2.4 | 27.2 |
| Precious Achiuwa | 98% | 29.3 | 13.9 | 8.3 | 1.6 | 0.4 | 1.1 | 1.0 | 1.3 | 23.9 |
| De'Andre Hunter | 98% | 27.6 | 12.2 | 5.1 | 1.6 | 1.7 | 0.8 | 0.2 | 1.3 | 19.0 |
| Daeqwon Plowden | 98% | 18.8 | 6.5 | 2.3 | 0.9 | 0.9 | 0.6 | 0.2 | 0.6 | 9.7 |
| Malik Monk | 96% | 16.2 | 8.7 | 1.7 | 2.8 | 1.1 | 0.5 | 0.3 | 1.1 | 13.2 |
| Jonathan Mogbo | 64% | 16.1 | 5.9 | 2.9 | 0.9 | 0.5 | 0.6 | 0.4 | 0.7 | 9.7 |
| Emanuel Sharp | 93% | 15.5 | 5.1 | 1.0 | 1.0 | 0.5 | 0.5 | 0.2 | 0.7 | 7.1 |
| Nique Clifford | 72% | 14.5 | 5.7 | 2.3 | 1.5 | 0.4 | 0.7 | 0.2 | 1.0 | 9.5 |
| Leaky Black | 52% | 11.6 | 3.1 | 2.1 | 0.8 | 0.3 | 0.5 | 0.3 | 0.4 | 6.0 |
| Alex Karaban | 58% | 9.1 | 2.4 | 1.7 | 0.7 | 0.0 | 0.3 | 0.2 | 0.5 | 4.8 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 33.9 | 18.5 | 5.1 | 3.3 | 3.2 | 1.3 | 0.5 | 1.4 | 26.9 |
| Dejounte Murray | 98% | 32.0 | 18.2 | 5.9 | 6.8 | 1.8 | 1.7 | 0.4 | 3.0 | 30.9 |
| Zion Williamson | 96% | 31.3 | 20.8 | 5.2 | 3.2 | 0.3 | 1.3 | 0.6 | 2.0 | 29.3 |
| Saddiq Bey | 96% | 27.9 | 15.1 | 4.4 | 2.1 | 2.1 | 0.8 | 0.1 | 1.1 | 21.6 |
| Jeremiah Fears | 98% | 25.7 | 14.7 | 3.5 | 3.2 | 1.4 | 1.2 | 0.4 | 2.1 | 21.4 |
| Derik Queen | 98% | 24.4 | 11.8 | 7.5 | 2.7 | 0.3 | 1.1 | 0.9 | 1.9 | 22.0 |
| Herbert Jones | 96% | 18.6 | 5.9 | 2.2 | 1.4 | 0.8 | 1.1 | 0.3 | 0.8 | 9.5 |
| Bennedict Mathurin | 98% | 16.6 | 8.0 | 3.1 | 1.4 | 0.5 | 0.5 | 0.2 | 1.1 | 12.5 |
| Karlo Matkovic | 86% | 13.7 | 5.5 | 3.4 | 0.8 | 0.4 | 0.4 | 0.8 | 0.6 | 9.7 |
| DeAndre Jordan | 58% | 13.6 | 4.1 | 5.6 | 0.8 | 0.0 | 0.4 | 0.7 | 0.7 | 10.4 |
| AJ Johnson | 8% | 12.7 | 5.5 | 2.3 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.9 |
| Bryce McGowens | 52% | 9.2 | 3.5 | 1.2 | 0.6 | 0.3 | 0.4 | 0.1 | 0.3 | 5.3 |
| Malik Dia | 35% | 8.6 | 3.7 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Jaron Pierre Jr. | 40% | 8.6 | 3.6 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 |
| Julian Reese | 30% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.5 | 6.0 |
| Trendon Watford | 26% | 8.2 | 3.3 | 1.5 | 0.9 | 0.1 | 0.3 | 0.2 | 0.6 | 5.7 |

</details>


### MEM @ POR
Out: Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ty Jerome AST under 5.5 | MEM @ POR | draftkings | 2.11 | 1.72 | 58.3% | 44.3% | 47.8% | +0.8% | +23.0% | 0.2% |
| Ja Morant AST over 6.5 | MEM @ POR | draftkings | 2.10 | 1.78 | 56.3% | 44.8% | 47.7% | +0.2% | +18.3% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Deni Avdija 5+ reb **+** Donovan Clingan 6+ pts | 59.3% | 1.69 | 1.77 | 1.53 | -9.6% |
| Jrue Holiday 15+ pra **+** Deni Avdija 5+ reb **+** Toumani Camara 6+ pts | 50.6% | 1.98 | 2.08 | 1.75 | -11.6% |
| Ty Jerome pa under 30.5 **+** Toumani Camara 6+ pts | 47.7% | 2.09 | 2.20 | 2.10 | +0.2% |
| Cedric Coward pts under 12.5 **+** Jrue Holiday 15+ pra | 42.3% | 2.36 | 2.48 | 2.43 | +2.7% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.2–119.5 | MEM 25% | 3.93 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o233.5 42% |
| Expected (weighted by chance each plays) | 110.2–119.9 | MEM 24% | 4.19 / 1.31 | POR -9.5 | 230.5 | POR -7.5 covers 56%; o233.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| John Tonje (POR) | Questionable | 55% | 8.6 | 3.5 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.8 | small |
| Jayson Kent (POR) | Questionable | 55% | 5.6 | 2.0 | 0.9 | 0.4 | 0.2 | 0.3 | 0.1 | 0.3 | 3.4 | small |
| Chris Youngblood (POR) | Questionable | 55% | 5.6 | 2.4 | 0.9 | 0.4 | 0.2 | 0.2 | 0.1 | 0.3 | 3.6 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 93% | 29.4 | 12.9 | 7.7 | 3.9 | 1.3 | 1.1 | 0.7 | 2.2 | 24.5 |
| Ty Jerome | 98% | 26.0 | 18.5 | 3.0 | 5.2 | 1.9 | 1.1 | 0.3 | 2.4 | 26.7 |
| Cedric Coward | 98% | 24.1 | 9.8 | 5.5 | 2.1 | 1.0 | 0.8 | 0.5 | 1.7 | 17.4 |
| Jaylen Wells | 98% | 23.7 | 9.6 | 2.8 | 1.2 | 1.2 | 1.0 | 0.2 | 1.1 | 13.6 |
| Jerami Grant | 98% | 22.0 | 9.3 | 2.5 | 1.5 | 1.1 | 0.8 | 0.7 | 1.4 | 13.2 |
| Zach Edey | 98% | 20.5 | 8.2 | 7.8 | 1.0 | 0.1 | 0.6 | 1.5 | 1.7 | 17.0 |
| Cam Spencer | 96% | 16.4 | 6.8 | 1.9 | 3.3 | 0.9 | 0.7 | 0.1 | 1.0 | 12.1 |
| Scotty Pippen Jr. | 97% | 15.3 | 7.3 | 2.1 | 2.7 | 0.6 | 1.1 | 0.3 | 1.6 | 12.2 |
| GG Jackson | 96% | 14.6 | 7.8 | 2.8 | 0.9 | 0.7 | 0.5 | 0.6 | 1.3 | 11.5 |
| Isaiah Stewart | 98% | 13.4 | 5.5 | 2.9 | 0.6 | 0.2 | 0.3 | 0.8 | 0.7 | 9.0 |
| Karim Lopez | 23% | 12.5 | 5.4 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.8 |
| Quinten Post | 88% | 12.2 | 4.3 | 2.1 | 0.7 | 0.4 | 0.3 | 0.4 | 0.7 | 7.1 |
| Olivier-Maxence Prosper | 30% | 11.2 | 5.8 | 2.2 | 0.5 | 0.4 | 0.5 | 0.2 | 0.6 | 8.5 |
| Javon Small | 86% | 9.4 | 4.0 | 1.5 | 1.3 | 0.3 | 0.4 | 0.1 | 0.8 | 6.8 |
| Carson Cooper | 35% | 8.6 | 3.7 | 1.5 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 6.0 |
| Jahmai Mashack | 38% | 8.2 | 2.6 | 1.1 | 0.9 | 0.1 | 0.4 | 0.2 | 0.7 | 4.6 |
| Taylor Hendricks | 52% | 8.0 | 3.3 | 1.6 | 0.4 | 0.2 | 0.5 | 0.2 | 0.4 | 5.3 |
| Kris Murray | 48% | 7.9 | 2.1 | 1.3 | 0.6 | 0.1 | 0.3 | 0.2 | 0.4 | 4.0 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 97% | 33.4 | 22.9 | 7.6 | 6.4 | 1.8 | 1.0 | 0.6 | 3.8 | 36.8 |
| Damian Lillard | 98% | 31.1 | 17.6 | 4.4 | 5.1 | 2.5 | 1.2 | 0.2 | 2.4 | 27.1 |
| Jrue Holiday | 98% | 29.9 | 14.5 | 4.7 | 5.5 | 2.3 | 1.1 | 0.2 | 2.4 | 24.7 |
| Toumani Camara | 98% | 29.7 | 12.1 | 4.5 | 2.0 | 2.1 | 1.2 | 0.5 | 1.4 | 18.6 |
| Ja Morant | 98% | 29.0 | 18.1 | 3.7 | 7.3 | 1.4 | 1.2 | 0.3 | 2.9 | 29.1 |
| Donovan Clingan | 98% | 23.4 | 10.6 | 10.6 | 1.9 | 1.1 | 0.6 | 1.8 | 1.1 | 23.1 |
| Scoot Henderson | 98% | 20.4 | 10.3 | 2.2 | 2.7 | 1.3 | 1.0 | 0.2 | 2.0 | 15.1 |
| Sidy Cissoko | 93% | 19.0 | 5.7 | 2.8 | 1.8 | 0.6 | 0.9 | 0.4 | 1.0 | 10.3 |
| Robert Williams III | 98% | 18.1 | 7.6 | 7.7 | 1.1 | 0.2 | 0.6 | 1.4 | 1.0 | 16.4 |
| Micah Potter | 52% | 11.5 | 5.2 | 3.3 | 0.7 | 0.6 | 0.3 | 0.3 | 0.7 | 9.2 |
| Vit Krejci | 96% | 9.7 | 3.6 | 1.4 | 0.8 | 0.4 | 0.4 | 0.1 | 0.4 | 5.8 |
| Branden Carlson | 16% | 8.7 | 3.6 | 1.5 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 5.9 |
| Yang Hansen | 52% | 6.2 | 2.3 | 1.7 | 0.4 | 0.1 | 0.1 | 0.2 | 0.6 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-29/`._
