# NBA model · Thu 29 Oct 2026 (US date)

Updated **Thu 29 Oct, 11:41 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

_No bets clear the edge threshold right now._

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jrue Holiday 3+ ast **+** Deni Avdija 5+ reb | MEM @ POR | 58.1% | 1.72 | 1.81 | 1.59 | -7.7% |
| James Harden 4+ reb **+** Donovan Mitchell 12+ pts | CLE @ ATL | 56.2% | 1.78 | 1.87 | 1.64 | -7.9% |
| Trey Murphy III 12+ pts **+** Jeremiah Fears 8+ pts | SAC @ NOP | 60.1% | 1.67 | 1.75 | 1.53 | -8.4% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| NOP win **+** Domantas Sabonis 9+ reb | SAC @ NOP | 53.8% | 1.86 | 1.95 | 1.74 | -6.6% |
| James Harden 4+ reb **+** Donovan Mitchell 3+ reb | CLE @ ATL | 51.3% | 1.95 | 2.05 | 1.81 | -6.9% |
| Nickeil Alexander-Walker reb under 3.5 **+** Donovan Mitchell 1+ 3pm | CLE @ ATL | 51.4% | 1.95 | 2.04 | 1.80 | -7.4% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Ty Jerome pts under 24.5 **+** Jrue Holiday 1+ 3pm | MEM @ POR | 47.8% | 2.09 | 2.20 | 2.09 | -0.1% |
| Ty Jerome pa under 30.5 **+** Toumani Camara 6+ pts | MEM @ POR | 47.5% | 2.10 | 2.21 | 2.10 | -0.2% |
| Cedric Coward pr under 19.5 **+** Jrue Holiday 1+ 3pm | MEM @ POR | 47.4% | 2.11 | 2.21 | 2.10 | -0.4% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Cedric Coward pts under 12.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 41.2% | 2.43 | 2.55 | 2.49 | +2.5% |
| Ty Jerome pra under 33.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 42.3% | 2.37 | 2.48 | 2.42 | +2.4% |
| Cedric Coward pts under 12.5 **+** Jrue Holiday 15+ pra | MEM @ POR | 42.4% | 2.36 | 2.48 | 2.41 | +2.3% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 5.5 | MEM @ POR | draftkings | 3.87 | 2.27 | 44.1% | 24.1% | 29.1% | +12.7% | +70.5% | 1.1% |
| Precious Achiuwa PTS over 14.5 | SAC @ NOP | draftkings | 3.60 | 2.41 | 41.5% | 26.0% | 29.8% | +7.5% | +49.5% | 0.7% |
| Ty Jerome PRA under 33.5 | MEM @ POR | draftkings | 1.92 | 1.31 | 76.6% | 48.7% | 55.7% | +6.8% | +46.8% | 1.8% |
| Cedric Coward PTS under 12.5 | MEM @ POR | draftkings | 1.97 | 1.34 | 74.4% | 47.4% | 54.2% | +6.8% | +46.7% | 1.7% |
| Jrue Holiday REB over 4.5 | MEM @ POR | draftkings | 3.05 | 2.08 | 48.0% | 30.6% | 35.0% | +6.7% | +46.4% | 0.8% |
| Jrue Holiday PRA over 24.5 | MEM @ POR | draftkings | 3.30 | 2.26 | 44.2% | 28.3% | 32.3% | +6.6% | +45.9% | 0.7% |
| Ty Jerome PR under 27.5 | MEM @ POR | draftkings | 1.88 | 1.30 | 76.7% | 49.6% | 56.4% | +6.2% | +44.5% | 1.8% |
| Ty Jerome PA under 30.5 | MEM @ POR | draftkings | 1.85 | 1.28 | 77.8% | 50.4% | 57.2% | +6.2% | +44.3% | 1.8% |
| Jrue Holiday AST over 4.5 | MEM @ POR | draftkings | 2.41 | 1.69 | 59.3% | 38.8% | 43.9% | +5.8% | +42.9% | 1.0% |
| Ty Jerome PTS under 24.5 | MEM @ POR | draftkings | 1.83 | 1.28 | 78.1% | 51.2% | 57.9% | +5.7% | +42.6% | 1.7% |
| Cedric Coward PR under 19.5 | MEM @ POR | draftkings | 1.83 | 1.30 | 76.9% | 51.0% | 57.5% | +5.4% | +41.1% | 1.6% |
| Jrue Holiday RA over 7.5 | MEM @ POR | draftkings | 1.93 | 1.38 | 72.3% | 48.4% | 54.4% | +5.2% | +39.9% | 1.4% |
| Cameron Boozer PTS under 15.5 | MEM @ POR | draftkings | 1.99 | 1.42 | 70.2% | 47.0% | 52.8% | +5.0% | +39.7% | 1.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CLE @ ATL | Fri 30 Oct 11:00 | 114.9–115.4 | CLE 48% | 2.08 / 1.93 | ATL -1.5 | 230.5 | ATL -1.5 covers 49%; o237.5 35% |
| SAC @ NOP | Fri 30 Oct 11:00 | 116.0–124.5 | SAC 27% | 3.65 / 1.38 | NOP -8.5 | 240.5 | NOP -5.5 covers 59%; o236.5 58% |
| MEM @ POR | Fri 30 Oct 13:00 | 110.2–119.5 | MEM 25% | 3.95 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o233.5 42% |

### CLE @ ATL
Out: Mouhamed Gueye (ATL)

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| James Harden 4+ reb **+** Donovan Mitchell 12+ pts | 56.2% | 1.78 | 1.87 | 1.64 | -7.9% |
| James Harden 4+ reb **+** Donovan Mitchell 3+ reb | 51.3% | 1.95 | 2.05 | 1.81 | -6.9% |
| Jalen Johnson ra under 16.5 **+** Evan Mobley 15+ pra | 47.0% | 2.13 | 2.23 | 2.06 | -3.2% |
| Jalen Johnson ra under 16.5 **+** James Harden 3+ reb | 39.7% | 2.52 | 2.64 | 2.46 | -2.1% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 98% | 37.1 | 26.2 | 5.5 | 4.4 | 3.0 | 1.5 | 0.4 | 3.2 | 36.2 |
| James Harden | 98% | 36.9 | 18.1 | 5.0 | 6.8 | 2.2 | 1.4 | 0.6 | 4.0 | 29.9 |
| Evan Mobley | 98% | 35.8 | 17.9 | 9.5 | 3.5 | 1.4 | 1.0 | 1.8 | 2.3 | 30.9 |
| Peyton Watson | 98% | 33.0 | 13.6 | 4.9 | 2.3 | 1.3 | 1.2 | 1.4 | 2.2 | 20.8 |
| Jarrett Allen | 98% | 29.0 | 14.1 | 8.5 | 1.6 | 0.1 | 1.1 | 1.3 | 1.5 | 24.2 |
| Sam Merrill | 98% | 24.0 | 7.7 | 2.3 | 1.7 | 1.3 | 0.7 | 0.1 | 0.8 | 11.6 |
| Jaylon Tyson | 93% | 19.7 | 7.9 | 3.6 | 1.9 | 0.9 | 0.6 | 0.3 | 1.1 | 13.4 |
| Meleek Thomas | 52% | 17.8 | 7.4 | 2.1 | 0.9 | 1.4 | 0.8 | 0.2 | 1.2 | 10.4 |
| Mario Hezonja | 91% | 15.1 | 5.6 | 3.0 | 0.9 | 0.5 | 0.5 | 0.2 | 0.8 | 9.5 |
| Craig Porter Jr. | 58% | 8.8 | 2.2 | 1.6 | 1.4 | 0.1 | 0.4 | 0.2 | 0.7 | 5.2 |
| Tyrese Proctor | 58% | 8.5 | 3.9 | 1.1 | 1.1 | 0.4 | 0.5 | 0.0 | 0.7 | 6.1 |
| Riley Minix | 26% | 8.3 | 3.2 | 1.1 | 0.5 | 0.2 | 0.3 | 0.1 | 0.4 | 4.8 |
| Thomas Bryant | 36% | 8.0 | 3.5 | 2.2 | 0.4 | 0.3 | 0.2 | 0.3 | 0.4 | 6.2 |
| Tristan Enaruna | 26% | 6.8 | 2.1 | 1.1 | 0.4 | 0.1 | 0.3 | 0.1 | 0.3 | 3.7 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 31.7 | 19.5 | 8.4 | 6.5 | 1.5 | 1.2 | 0.4 | 2.8 | 34.4 |
| Nickeil Alexander-Walker | 98% | 29.1 | 17.8 | 2.9 | 3.1 | 2.7 | 1.1 | 0.4 | 1.9 | 23.7 |
| Dyson Daniels | 98% | 27.9 | 10.7 | 5.8 | 4.4 | 0.6 | 2.1 | 0.3 | 1.6 | 20.9 |
| CJ McCollum | 98% | 27.3 | 17.1 | 2.7 | 3.1 | 2.2 | 0.9 | 0.5 | 1.8 | 22.9 |
| Onyeka Okongwu | 98% | 26.8 | 11.8 | 6.4 | 2.4 | 1.3 | 1.0 | 0.8 | 1.2 | 20.6 |
| Aaron Wiggins | 91% | 21.5 | 9.2 | 2.5 | 1.4 | 1.3 | 0.9 | 0.2 | 0.9 | 13.2 |
| Luguentz Dort | 98% | 20.1 | 7.2 | 2.5 | 1.2 | 1.1 | 0.8 | 0.2 | 0.6 | 10.8 |
| Jock Landale | 98% | 17.6 | 7.7 | 4.2 | 1.8 | 0.6 | 0.5 | 0.5 | 0.7 | 13.7 |
| Kingston Flemings | 93% | 15.0 | 5.4 | 2.2 | 2.9 | 0.3 | 0.4 | 0.2 | 1.3 | 10.6 |
| Corey Kispert | 63% | 7.9 | 4.3 | 1.1 | 0.7 | 0.5 | 0.1 | 0.1 | 0.3 | 6.0 |
| Jalen Wilson | 76% | 7.5 | 3.1 | 1.2 | 0.5 | 0.3 | 0.2 | 0.0 | 0.3 | 4.8 |
| Asa Newell | 58% | 6.7 | 3.0 | 1.4 | 0.4 | 0.2 | 0.2 | 0.2 | 0.3 | 4.8 |
| Dorian Finney-Smith | 58% | 6.6 | 1.9 | 1.1 | 0.4 | 0.1 | 0.2 | 0.1 | 0.3 | 3.3 |
| Keshon Gilbert | 88% | 6.0 | 1.7 | 0.8 | 0.8 | 0.1 | 0.2 | 0.2 | 0.4 | 3.2 |
| Zuby Ejiofor | 58% | 5.7 | 2.3 | 1.1 | 0.5 | 0.2 | 0.2 | 0.1 | 0.3 | 3.9 |
| RayJ Dennis | 63% | 5.4 | 2.1 | 0.7 | 0.9 | 0.1 | 0.2 | 0.1 | 0.3 | 3.6 |

</details>


### SAC @ NOP
Out: Yves Missi (NOP), Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray 3PM over 1.5 | SAC @ NOP | draftkings | 2.34 | 1.90 | 52.7% | 39.9% | 43.1% | +0.9% | +23.3% | 0.2% |
| Precious Achiuwa PR over 18.5 | SAC @ NOP | draftkings | 1.83 | 1.52 | 66.0% | 51.5% | 55.1% | +0.7% | +20.4% | 0.2% |
| Zach LaVine PA under 25.5 | SAC @ NOP | draftkings | 1.94 | 1.62 | 61.7% | 48.1% | 51.5% | +0.1% | +20.0% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Trey Murphy III 12+ pts **+** Jeremiah Fears 8+ pts | 60.1% | 1.67 | 1.75 | 1.53 | -8.4% |
| NOP win **+** Domantas Sabonis 9+ reb | 53.8% | 1.86 | 1.95 | 1.74 | -6.6% |
| Precious Achiuwa 19+ pr **+** Domantas Sabonis 9+ reb | 46.1% | 2.17 | 2.28 | 2.08 | -4.0% |
| Precious Achiuwa 11+ pts **+** Trey Murphy III 2+ 3pm | 40.9% | 2.45 | 2.57 | 2.39 | -2.2% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.0–124.5 | SAC 27% | 3.65 / 1.38 | NOP -8.5 | 240.5 | NOP -5.5 covers 59%; o236.5 58% |
| Expected (weighted by chance each plays) | 115.8–125.6 | SAC 24% | 4.10 / 1.32 | NOP -9.5 | 241.5 | NOP -5.5 covers 62%; o236.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Poole (NOP) | Day-To-Day | 70% | 18.1 | 9.3 | 1.9 | 2.5 | 1.6 | 0.6 | 0.4 | 1.2 | 13.7 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 93% | 34.6 | 20.7 | 3.7 | 4.6 | 2.2 | 1.1 | 0.4 | 2.8 | 29.0 |
| Domantas Sabonis | 98% | 33.8 | 19.3 | 14.4 | 5.6 | 0.3 | 0.9 | 0.4 | 2.6 | 39.3 |
| Zach LaVine | 98% | 33.4 | 21.0 | 3.4 | 2.9 | 2.6 | 0.8 | 0.2 | 2.4 | 27.3 |
| Precious Achiuwa | 98% | 29.3 | 14.0 | 8.4 | 1.6 | 0.4 | 1.1 | 1.0 | 1.3 | 24.0 |
| De'Andre Hunter | 98% | 27.5 | 12.2 | 5.1 | 1.6 | 1.7 | 0.8 | 0.2 | 1.3 | 18.9 |
| Daeqwon Plowden | 98% | 18.7 | 6.4 | 2.3 | 0.9 | 0.9 | 0.6 | 0.2 | 0.6 | 9.7 |
| Malik Monk | 96% | 16.3 | 8.8 | 1.7 | 2.8 | 1.1 | 0.5 | 0.3 | 1.1 | 13.3 |
| Jonathan Mogbo | 64% | 16.1 | 5.8 | 2.9 | 0.9 | 0.5 | 0.6 | 0.4 | 0.7 | 9.7 |
| Emanuel Sharp | 93% | 15.4 | 5.1 | 1.0 | 1.0 | 0.5 | 0.6 | 0.2 | 0.7 | 7.1 |
| Nique Clifford | 72% | 14.7 | 5.8 | 2.3 | 1.5 | 0.4 | 0.7 | 0.2 | 1.0 | 9.5 |
| Leaky Black | 52% | 11.6 | 3.1 | 2.0 | 0.8 | 0.3 | 0.5 | 0.3 | 0.4 | 6.0 |
| Alex Karaban | 58% | 9.1 | 2.5 | 1.7 | 0.7 | 0.0 | 0.3 | 0.2 | 0.5 | 4.8 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 35.2 | 20.1 | 5.4 | 3.4 | 3.4 | 1.4 | 0.5 | 1.5 | 28.9 |
| Dejounte Murray | 98% | 33.0 | 19.1 | 6.0 | 7.1 | 1.8 | 1.9 | 0.4 | 3.1 | 32.2 |
| Zion Williamson | 91% | 32.0 | 21.4 | 5.5 | 3.2 | 0.2 | 1.3 | 0.7 | 2.1 | 30.2 |
| Saddiq Bey | 91% | 28.8 | 15.9 | 4.8 | 2.0 | 2.2 | 0.9 | 0.1 | 1.2 | 22.8 |
| Jeremiah Fears | 98% | 26.1 | 14.8 | 3.7 | 3.0 | 1.4 | 1.2 | 0.4 | 2.0 | 21.5 |
| Derik Queen | 98% | 25.0 | 12.1 | 7.7 | 2.9 | 0.4 | 1.1 | 1.0 | 1.9 | 22.7 |
| Bennedict Mathurin | 98% | 18.7 | 9.0 | 3.6 | 1.6 | 0.6 | 0.6 | 0.2 | 1.1 | 14.2 |
| Herbert Jones | 91% | 17.8 | 5.6 | 2.1 | 1.2 | 0.7 | 1.1 | 0.3 | 0.7 | 8.9 |
| DeAndre Jordan | 48% | 14.1 | 4.2 | 5.6 | 0.8 | 0.0 | 0.3 | 0.7 | 0.7 | 10.6 |
| AJ Johnson | 8% | 12.4 | 5.2 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.5 |
| Bryce McGowens | 38% | 12.0 | 4.5 | 1.4 | 0.8 | 0.3 | 0.5 | 0.2 | 0.4 | 6.7 |
| Karlo Matkovic | 76% | 11.8 | 4.6 | 3.0 | 0.6 | 0.3 | 0.4 | 0.7 | 0.5 | 8.2 |
| Malik Dia | 35% | 8.6 | 3.7 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Julian Reese | 35% | 8.6 | 3.6 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Jaron Pierre Jr. | 40% | 8.5 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Trendon Watford | 35% | 8.4 | 3.3 | 1.6 | 1.0 | 0.1 | 0.3 | 0.2 | 0.6 | 5.8 |

</details>


### MEM @ POR
Out: Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3PM under 2.5 | MEM @ POR | draftkings | 2.24 | 1.78 | 56.2% | 41.7% | 45.4% | +1.6% | +25.9% | 0.3% |
| Ty Jerome AST under 5.5 | MEM @ POR | draftkings | 2.11 | 1.71 | 58.3% | 44.3% | 47.8% | +0.9% | +23.1% | 0.2% |
| Jrue Holiday PA over 16.5 | MEM @ POR | draftkings | 1.93 | 1.60 | 62.4% | 48.3% | 51.8% | +0.3% | +20.7% | 0.1% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Jrue Holiday 3+ ast **+** Deni Avdija 5+ reb | 58.1% | 1.72 | 1.81 | 1.59 | -7.7% |
| Jrue Holiday 15+ pra **+** Deni Avdija 5+ reb **+** Toumani Camara 6+ pts | 50.6% | 1.98 | 2.08 | 1.74 | -11.9% |
| Ty Jerome pts under 24.5 **+** Jrue Holiday 1+ 3pm | 47.8% | 2.09 | 2.20 | 2.09 | -0.1% |
| Cedric Coward pts under 12.5 **+** Jrue Holiday 3+ ast | 41.2% | 2.43 | 2.55 | 2.49 | +2.5% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.2–119.5 | MEM 25% | 3.95 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o233.5 42% |
| Expected (weighted by chance each plays) | 110.2–120.0 | MEM 24% | 4.21 / 1.31 | POR -9.5 | 230.5 | POR -7.5 covers 56%; o233.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| John Tonje (POR) | Questionable | 55% | 8.6 | 3.5 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.8 | small |
| Jayson Kent (POR) | Questionable | 55% | 5.6 | 2.0 | 0.9 | 0.4 | 0.2 | 0.3 | 0.1 | 0.4 | 3.4 | small |
| Chris Youngblood (POR) | Questionable | 55% | 5.6 | 2.3 | 0.9 | 0.4 | 0.2 | 0.2 | 0.1 | 0.3 | 3.6 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 93% | 29.5 | 12.9 | 7.7 | 3.9 | 1.3 | 1.0 | 0.7 | 2.2 | 24.5 |
| Ty Jerome | 98% | 26.0 | 18.5 | 3.0 | 5.2 | 1.9 | 1.1 | 0.3 | 2.4 | 26.7 |
| Cedric Coward | 98% | 24.0 | 9.7 | 5.5 | 2.1 | 1.0 | 0.8 | 0.5 | 1.7 | 17.2 |
| Jaylen Wells | 98% | 23.8 | 9.6 | 2.8 | 1.2 | 1.2 | 1.0 | 0.2 | 1.1 | 13.7 |
| Jerami Grant | 98% | 21.9 | 9.2 | 2.4 | 1.5 | 1.1 | 0.8 | 0.7 | 1.5 | 13.2 |
| Zach Edey | 98% | 20.5 | 8.2 | 7.7 | 1.0 | 0.1 | 0.6 | 1.5 | 1.7 | 16.9 |
| Cam Spencer | 96% | 16.4 | 6.8 | 1.9 | 3.3 | 0.9 | 0.7 | 0.1 | 1.0 | 12.1 |
| Scotty Pippen Jr. | 97% | 15.3 | 7.3 | 2.1 | 2.7 | 0.7 | 1.1 | 0.3 | 1.6 | 12.1 |
| GG Jackson | 96% | 14.5 | 7.7 | 2.8 | 0.9 | 0.7 | 0.5 | 0.6 | 1.3 | 11.4 |
| Isaiah Stewart | 98% | 13.5 | 5.5 | 2.9 | 0.6 | 0.2 | 0.3 | 0.8 | 0.7 | 9.0 |
| Karim Lopez | 23% | 12.3 | 5.4 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.7 |
| Quinten Post | 88% | 12.2 | 4.4 | 2.1 | 0.7 | 0.4 | 0.3 | 0.4 | 0.7 | 7.1 |
| Olivier-Maxence Prosper | 30% | 11.2 | 5.8 | 2.2 | 0.5 | 0.4 | 0.5 | 0.2 | 0.6 | 8.5 |
| Javon Small | 86% | 9.4 | 4.0 | 1.5 | 1.3 | 0.3 | 0.4 | 0.1 | 0.8 | 6.8 |
| Carson Cooper | 35% | 8.6 | 3.8 | 1.6 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 6.1 |
| Jahmai Mashack | 38% | 8.1 | 2.5 | 1.1 | 0.9 | 0.1 | 0.4 | 0.2 | 0.7 | 4.5 |
| Taylor Hendricks | 52% | 8.0 | 3.3 | 1.6 | 0.4 | 0.2 | 0.5 | 0.2 | 0.4 | 5.3 |
| Kris Murray | 48% | 7.9 | 2.1 | 1.3 | 0.6 | 0.1 | 0.3 | 0.2 | 0.3 | 4.0 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 97% | 33.3 | 22.9 | 7.5 | 6.3 | 1.8 | 1.0 | 0.6 | 3.8 | 36.8 |
| Damian Lillard | 98% | 31.1 | 17.5 | 4.3 | 5.0 | 2.5 | 1.2 | 0.2 | 2.4 | 26.8 |
| Jrue Holiday | 98% | 30.0 | 14.6 | 4.7 | 5.5 | 2.3 | 1.1 | 0.2 | 2.4 | 24.8 |
| Toumani Camara | 98% | 29.8 | 12.0 | 4.6 | 2.0 | 2.1 | 1.2 | 0.5 | 1.4 | 18.6 |
| Ja Morant | 98% | 29.0 | 18.1 | 3.8 | 7.3 | 1.4 | 1.2 | 0.3 | 3.0 | 29.1 |
| Donovan Clingan | 98% | 23.5 | 10.6 | 10.7 | 1.9 | 1.1 | 0.6 | 1.8 | 1.1 | 23.2 |
| Scoot Henderson | 98% | 20.4 | 10.2 | 2.1 | 2.7 | 1.2 | 1.0 | 0.2 | 2.0 | 15.0 |
| Sidy Cissoko | 93% | 18.9 | 5.6 | 2.8 | 1.8 | 0.6 | 0.9 | 0.4 | 1.0 | 10.2 |
| Robert Williams III | 98% | 18.1 | 7.6 | 7.7 | 1.1 | 0.2 | 0.6 | 1.5 | 1.0 | 16.5 |
| Micah Potter | 52% | 11.5 | 5.2 | 3.4 | 0.7 | 0.6 | 0.4 | 0.2 | 0.7 | 9.2 |
| Vit Krejci | 96% | 9.7 | 3.7 | 1.4 | 0.8 | 0.5 | 0.4 | 0.1 | 0.4 | 5.9 |
| Branden Carlson | 16% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 |
| Yang Hansen | 52% | 6.1 | 2.3 | 1.6 | 0.4 | 0.1 | 0.1 | 0.2 | 0.6 | 4.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-29/`._
