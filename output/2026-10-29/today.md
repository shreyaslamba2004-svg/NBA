# NBA model · Thu 29 Oct 2026 (US date)

Updated **Fri 30 Oct, 04:51 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Robert Williams III REB over 8.5 | MEM @ POR | draftkings | 3.57 | 2.48 | 40.4% | 26.2% | 29.7% | +6.2% | +44.2% | 0.6% |

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Sam Merrill 3pm under 2.5 **+** Evan Mobley 4+ reb | CLE @ ATL | 60.6% | 1.65 | 1.73 | 1.62 | -1.7% |
| NOP win **+** Domantas Sabonis 8+ reb | SAC @ NOP | 58.3% | 1.72 | 1.80 | 1.60 | -6.8% |
| NOP win **+** Domantas Sabonis 20+ pra | SAC @ NOP | 60.6% | 1.65 | 1.73 | 1.54 | -6.9% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Sam Merrill 3pm under 2.5 **+** Onyeka Okongwu 6+ pts | CLE @ ATL | 55.6% | 1.80 | 1.89 | 1.79 | -0.6% |
| Sam Merrill 3pm under 2.5 **+** Donovan Mitchell 12+ pts | CLE @ ATL | 59.2% | 1.69 | 1.77 | 1.67 | -1.4% |
| Sam Merrill 3pm under 2.5 **+** Donovan Mitchell 20+ pra | CLE @ ATL | 58.7% | 1.70 | 1.79 | 1.68 | -1.5% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Damian Lillard pts under 20.5 **+** Deni Avdija 3+ ast | MEM @ POR | 48.5% | 2.06 | 2.16 | 2.04 | -0.8% |
| Sam Merrill 3pm under 2.5 **+** Jalen Johnson 1+ 3pm | CLE @ ATL | 50.0% | 2.00 | 2.10 | 1.97 | -1.2% |
| Jrue Holiday 8+ ra **+** Ja Morant 4+ ast | MEM @ POR | 47.2% | 2.12 | 2.23 | 2.09 | -1.3% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Cedric Coward pts under 12.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 40.5% | 2.47 | 2.59 | 2.50 | +1.3% |
| Damian Lillard pts under 20.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 41.8% | 2.39 | 2.51 | 2.42 | +1.1% |
| Ty Jerome pra under 33.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 41.4% | 2.42 | 2.54 | 2.43 | +0.6% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 5.5 | MEM @ POR | draftkings | 3.90 | 2.38 | 42.0% | 24.0% | 28.5% | +11.1% | +63.9% | 0.9% |
| Precious Achiuwa PTS over 14.5 | SAC @ NOP | draftkings | 3.61 | 2.41 | 41.5% | 25.9% | 29.8% | +7.6% | +49.9% | 0.7% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CLE @ ATL | Fri 30 Oct 11:00 | 116.2–117.0 | CLE 47% | 2.11 / 1.90 | ATL -1.5 | 233.5 | ATL -1.5 covers 49%; o237.5 40% |
| SAC @ NOP | Fri 30 Oct 11:00 | 115.6–122.8 | SAC 30% | 3.30 / 1.43 | NOP -7.5 | 238.5 | NOP -5.5 covers 55%; o235.5 56% |
| MEM @ POR | Fri 30 Oct 13:00 | 110.2–119.5 | MEM 25% | 3.93 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o233.5 42% |

### CLE @ ATL
Out: Mouhamed Gueye (ATL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson PA under 29.5 | CLE @ ATL | draftkings | 1.93 | 1.59 | 62.7% | 48.5% | 52.1% | +0.3% | +20.9% | 0.1% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Sam Merrill 3pm under 2.5 **+** Evan Mobley 4+ reb | 60.6% | 1.65 | 1.73 | 1.62 | -1.7% |
| Sam Merrill 3pm under 2.5 **+** Onyeka Okongwu 6+ pts | 55.6% | 1.80 | 1.89 | 1.79 | -0.6% |
| Sam Merrill 3pm under 2.5 **+** Jalen Johnson 1+ 3pm | 50.0% | 2.00 | 2.10 | 1.97 | -1.2% |
| Jalen Johnson pra under 39.5 **+** Onyeka Okongwu 6+ pts | 44.6% | 2.24 | 2.35 | 2.16 | -3.6% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.2–117.0 | CLE 47% | 2.11 / 1.90 | ATL -1.5 | 233.5 | ATL -1.5 covers 49%; o237.5 40% |
| Expected (weighted by chance each plays) | 116.8–116.8 | CLE 49% | 2.02 / 1.98 | ATL +0.5 | 233.5 | ATL -1.5 covers 48%; o237.5 42% |
| if Jaylon Tyson plays | 116.6–117.6 | CLE 47% | 2.14 / 1.88 | ATL -1.5 | 234.5 | ATL -1.5 covers 50%; o237.5 43% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Questionable | 55% | 11.5 | 4.5 | 1.8 | 0.8 | 0.4 | 0.3 | 0.1 | 0.5 | 7.2 | small |
| Keshon Gilbert (ATL) | Questionable | 55% | 8.2 | 2.3 | 1.0 | 1.0 | 0.1 | 0.3 | 0.3 | 0.6 | 4.3 | small |
| Jaylon Tyson (CLE) | Questionable | 55% | 21.1 | 8.4 | 3.7 | 1.9 | 1.0 | 0.6 | 0.3 | 1.2 | 14.0 | full tables below |
| Meleek Thomas (CLE) | Questionable | 55% | 19.8 | 8.1 | 2.8 | 1.0 | 0.9 | 0.7 | 0.1 | 1.2 | 11.9 | small |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.4 | 19.6 | 4.6 | 6.3 | 2.4 | 1.4 | 0.6 | 3.8 | 30.5 |
| Donovan Mitchell | 98% | 36.3 | 27.1 | 5.2 | 4.8 | 2.9 | 1.5 | 0.3 | 3.0 | 37.1 |
| Evan Mobley | 98% | 35.1 | 18.9 | 9.2 | 3.4 | 1.4 | 1.0 | 1.7 | 2.1 | 31.6 |
| Peyton Watson | 98% | 33.0 | 15.8 | 4.8 | 2.2 | 1.5 | 1.1 | 1.1 | 2.3 | 22.9 |
| Jarrett Allen | 98% | 29.9 | 14.1 | 8.9 | 1.6 | 0.1 | 1.0 | 1.5 | 1.4 | 24.6 |
| Sam Merrill | 98% | 25.9 | 9.3 | 2.4 | 1.8 | 1.7 | 0.7 | 0.1 | 0.8 | 13.5 |
| Mario Hezonja | 93% | 18.2 | 6.9 | 3.5 | 1.0 | 0.7 | 0.6 | 0.3 | 0.9 | 11.5 |
| Craig Porter Jr. | 52% | 12.7 | 3.3 | 2.3 | 1.9 | 0.2 | 0.6 | 0.4 | 0.9 | 7.5 |
| Tyrese Proctor | 64% | 12.2 | 5.4 | 1.6 | 1.5 | 0.6 | 0.6 | 0.1 | 0.9 | 8.4 |
| Thomas Bryant | 30% | 12.1 | 5.5 | 3.3 | 0.6 | 0.5 | 0.3 | 0.4 | 0.5 | 9.3 |
| Riley Minix | 23% | 10.0 | 4.0 | 1.2 | 0.6 | 0.4 | 0.3 | 0.2 | 0.5 | 5.8 |
| Tristan Enaruna | 23% | 8.6 | 2.9 | 1.4 | 0.5 | 0.2 | 0.4 | 0.1 | 0.4 | 4.9 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 35.2 | 20.6 | 9.0 | 7.2 | 1.6 | 1.2 | 0.5 | 3.0 | 36.8 |
| Nickeil Alexander-Walker | 98% | 32.6 | 18.9 | 3.0 | 3.1 | 3.1 | 1.2 | 0.5 | 2.1 | 25.0 |
| Onyeka Okongwu | 98% | 30.4 | 12.7 | 6.8 | 2.7 | 1.5 | 1.1 | 0.9 | 1.3 | 22.1 |
| Dyson Daniels | 98% | 30.3 | 11.2 | 6.0 | 4.8 | 0.6 | 2.2 | 0.3 | 1.5 | 21.9 |
| CJ McCollum | 98% | 28.1 | 17.0 | 2.6 | 2.9 | 2.2 | 0.9 | 0.5 | 1.8 | 22.5 |
| Aaron Wiggins | 91% | 25.9 | 11.2 | 3.2 | 1.7 | 1.6 | 1.0 | 0.3 | 1.0 | 16.1 |
| Luguentz Dort | 98% | 23.1 | 8.0 | 2.8 | 1.4 | 1.2 | 0.8 | 0.2 | 0.7 | 12.2 |
| Kingston Flemings | 96% | 21.7 | 7.9 | 3.3 | 3.9 | 0.7 | 0.7 | 0.3 | 1.6 | 15.1 |
| Jock Landale | 98% | 18.1 | 7.7 | 4.3 | 1.6 | 0.7 | 0.5 | 0.5 | 0.8 | 13.6 |
| Corey Kispert | 52% | 9.7 | 4.8 | 1.3 | 0.8 | 0.6 | 0.2 | 0.1 | 0.4 | 6.8 |
| Asa Newell | 52% | 8.4 | 3.5 | 1.6 | 0.5 | 0.2 | 0.3 | 0.2 | 0.4 | 5.6 |
| RayJ Dennis | 34% | 8.3 | 2.9 | 1.1 | 1.2 | 0.3 | 0.3 | 0.1 | 0.5 | 5.2 |
| Dorian Finney-Smith | 52% | 7.4 | 2.1 | 1.1 | 0.4 | 0.1 | 0.2 | 0.1 | 0.3 | 3.7 |
| Zuby Ejiofor | 28% | 6.1 | 2.5 | 1.1 | 0.5 | 0.2 | 0.2 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>if Jaylon Tyson plays: both teams</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 35.2 | 20.6 | 9.0 | 7.2 | 1.6 | 1.2 | 0.5 | 3.0 | 36.8 |
| Nickeil Alexander-Walker (ATL) | 98% | 32.5 | 19.0 | 3.0 | 3.1 | 3.1 | 1.2 | 0.5 | 2.1 | 25.1 |
| Dyson Daniels (ATL) | 98% | 30.4 | 11.4 | 6.0 | 4.8 | 0.6 | 2.2 | 0.3 | 1.5 | 22.1 |
| Onyeka Okongwu (ATL) | 98% | 30.4 | 12.6 | 6.8 | 2.6 | 1.5 | 1.1 | 0.9 | 1.3 | 22.0 |
| CJ McCollum (ATL) | 98% | 28.2 | 17.0 | 2.6 | 2.9 | 2.2 | 0.9 | 0.5 | 1.8 | 22.5 |
| Aaron Wiggins (ATL) | 91% | 25.9 | 11.3 | 3.2 | 1.7 | 1.7 | 1.0 | 0.3 | 1.0 | 16.2 |
| Luguentz Dort (ATL) | 98% | 23.0 | 8.0 | 2.8 | 1.4 | 1.2 | 0.8 | 0.2 | 0.7 | 12.1 |
| Kingston Flemings (ATL) | 96% | 21.5 | 7.8 | 3.3 | 3.9 | 0.7 | 0.6 | 0.3 | 1.6 | 15.0 |
| Jock Landale (ATL) | 98% | 18.2 | 7.7 | 4.3 | 1.6 | 0.7 | 0.5 | 0.5 | 0.8 | 13.6 |
| Corey Kispert (ATL) | 52% | 9.6 | 4.8 | 1.3 | 0.8 | 0.6 | 0.2 | 0.1 | 0.4 | 6.8 |
| RayJ Dennis (ATL) | 34% | 8.4 | 3.0 | 1.1 | 1.1 | 0.3 | 0.3 | 0.1 | 0.5 | 5.2 |
| Asa Newell (ATL) | 52% | 8.3 | 3.4 | 1.7 | 0.5 | 0.2 | 0.3 | 0.2 | 0.4 | 5.6 |
| Dorian Finney-Smith (ATL) | 52% | 7.4 | 2.1 | 1.1 | 0.5 | 0.1 | 0.2 | 0.1 | 0.3 | 3.7 |
| Zuby Ejiofor (ATL) | 28% | 6.0 | 2.5 | 1.1 | 0.5 | 0.2 | 0.2 | 0.1 | 0.3 | 4.0 |
| Donovan Mitchell (CLE) | 98% | 35.2 | 26.5 | 5.1 | 4.4 | 2.8 | 1.4 | 0.3 | 3.0 | 35.9 |
| James Harden (CLE) | 98% | 34.9 | 18.3 | 4.5 | 6.0 | 2.3 | 1.3 | 0.5 | 3.7 | 28.9 |
| Evan Mobley (CLE) | 98% | 33.8 | 18.1 | 8.9 | 3.3 | 1.3 | 1.0 | 1.6 | 2.0 | 30.3 |
| Peyton Watson (CLE) | 98% | 31.0 | 14.4 | 4.6 | 2.0 | 1.4 | 1.0 | 1.1 | 2.2 | 21.1 |
| Jarrett Allen (CLE) | 98% | 28.5 | 13.4 | 8.5 | 1.5 | 0.1 | 1.0 | 1.4 | 1.3 | 23.4 |
| Sam Merrill (CLE) | 98% | 23.2 | 8.1 | 2.1 | 1.6 | 1.4 | 0.7 | 0.1 | 0.7 | 11.7 |
| Jaylon Tyson (CLE) | 100% | 21.1 | 8.4 | 3.7 | 1.9 | 1.0 | 0.6 | 0.3 | 1.2 | 14.0 |
| Mario Hezonja (CLE) | 93% | 15.9 | 5.9 | 3.2 | 0.9 | 0.6 | 0.5 | 0.2 | 0.8 | 10.0 |
| Craig Porter Jr. (CLE) | 52% | 9.8 | 2.7 | 1.8 | 1.4 | 0.1 | 0.5 | 0.3 | 0.7 | 5.9 |
| Tyrese Proctor (CLE) | 64% | 9.6 | 4.5 | 1.2 | 1.3 | 0.5 | 0.5 | 0.1 | 0.7 | 7.0 |
| Thomas Bryant (CLE) | 30% | 9.1 | 4.2 | 2.5 | 0.4 | 0.3 | 0.2 | 0.3 | 0.4 | 7.1 |
| Riley Minix (CLE) | 23% | 7.1 | 2.8 | 0.9 | 0.4 | 0.2 | 0.2 | 0.1 | 0.3 | 4.1 |
| Tristan Enaruna (CLE) | 23% | 6.2 | 2.1 | 1.1 | 0.4 | 0.1 | 0.3 | 0.1 | 0.3 | 3.6 |

</details>


### SAC @ NOP
Out: Yves Missi (NOP), Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PR over 18.5 | SAC @ NOP | draftkings | 1.83 | 1.52 | 65.9% | 51.4% | 55.0% | +0.9% | +20.8% | 0.3% |
| Darius Acuff Jr. PA under 28.5 | SAC @ NOP | draftkings | 1.81 | 1.50 | 66.5% | 51.7% | 55.4% | +0.1% | +20.1% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| NOP win **+** Domantas Sabonis 8+ reb | 58.3% | 1.72 | 1.80 | 1.60 | -6.8% |
| NOP win **+** Jeremiah Fears 8+ pts | 53.0% | 1.89 | 1.98 | 1.79 | -5.1% |
| Precious Achiuwa 11+ pts **+** Domantas Sabonis 25+ pra | 47.0% | 2.13 | 2.23 | 2.10 | -1.4% |
| Precious Achiuwa 11+ pts **+** Trey Murphy III 2+ 3pm | 41.5% | 2.41 | 2.53 | 2.38 | -1.5% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.6–122.8 | SAC 30% | 3.30 / 1.43 | NOP -7.5 | 238.5 | NOP -5.5 covers 55%; o235.5 56% |
| Expected (weighted by chance each plays) | 115.6–123.2 | SAC 29% | 3.39 / 1.42 | NOP -7.5 | 238.5 | NOP -5.5 covers 56%; o235.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Poole (NOP) | Doubtful | 20% | 15.2 | 7.5 | 1.6 | 2.0 | 1.1 | 0.6 | 0.3 | 0.9 | 11.1 | small |
| Jaron Pierre Jr. (NOP) | Questionable | 55% | 8.7 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |
| Malik Dia (NOP) | Questionable | 55% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 93% | 34.8 | 20.9 | 3.9 | 4.7 | 2.1 | 1.1 | 0.4 | 2.8 | 29.4 |
| Domantas Sabonis | 98% | 34.5 | 18.8 | 14.4 | 5.9 | 0.4 | 1.0 | 0.4 | 2.6 | 39.1 |
| Zach LaVine | 98% | 34.4 | 21.9 | 3.5 | 2.9 | 2.8 | 0.9 | 0.3 | 2.3 | 28.4 |
| Precious Achiuwa | 98% | 29.8 | 14.0 | 8.3 | 1.7 | 0.4 | 1.1 | 1.0 | 1.3 | 24.0 |
| De'Andre Hunter | 98% | 27.7 | 11.8 | 5.2 | 1.5 | 1.7 | 0.7 | 0.2 | 1.2 | 18.5 |
| Daeqwon Plowden | 98% | 18.2 | 5.9 | 2.1 | 0.9 | 0.9 | 0.5 | 0.2 | 0.6 | 8.9 |
| Jonathan Mogbo | 64% | 16.0 | 5.6 | 2.9 | 0.9 | 0.5 | 0.5 | 0.3 | 0.7 | 9.4 |
| Malik Monk | 96% | 15.7 | 8.2 | 1.6 | 2.8 | 1.0 | 0.5 | 0.3 | 1.1 | 12.5 |
| Emanuel Sharp | 93% | 15.5 | 5.0 | 1.0 | 1.0 | 0.6 | 0.5 | 0.2 | 0.6 | 7.0 |
| Nique Clifford | 72% | 12.4 | 4.8 | 1.9 | 1.2 | 0.4 | 0.5 | 0.2 | 0.9 | 8.0 |
| Leaky Black | 52% | 11.1 | 3.0 | 2.1 | 0.8 | 0.2 | 0.5 | 0.4 | 0.4 | 6.0 |
| Alex Karaban | 58% | 9.3 | 2.5 | 1.8 | 0.6 | 0.0 | 0.3 | 0.3 | 0.5 | 4.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 34.4 | 18.8 | 5.2 | 3.4 | 3.1 | 1.4 | 0.5 | 1.6 | 27.4 |
| Dejounte Murray | 98% | 32.5 | 19.0 | 5.9 | 6.9 | 1.7 | 1.9 | 0.4 | 3.0 | 31.8 |
| Zion Williamson | 96% | 32.3 | 21.4 | 5.6 | 3.3 | 0.2 | 1.2 | 0.7 | 2.1 | 30.4 |
| Saddiq Bey | 96% | 28.6 | 16.0 | 4.7 | 2.2 | 2.1 | 0.9 | 0.2 | 1.0 | 22.9 |
| Jeremiah Fears | 98% | 26.5 | 14.8 | 3.7 | 3.4 | 1.4 | 1.2 | 0.4 | 2.1 | 21.8 |
| Derik Queen | 98% | 26.3 | 12.7 | 8.2 | 3.0 | 0.3 | 1.1 | 1.0 | 2.2 | 23.9 |
| Herbert Jones | 96% | 19.7 | 6.0 | 2.3 | 1.6 | 0.8 | 1.1 | 0.4 | 0.7 | 9.9 |
| Bennedict Mathurin | 98% | 18.3 | 8.8 | 3.4 | 1.6 | 0.6 | 0.5 | 0.2 | 1.2 | 13.8 |
| Karlo Matkovic | 86% | 15.5 | 5.8 | 3.9 | 0.9 | 0.5 | 0.5 | 1.0 | 0.6 | 10.6 |
| DeAndre Jordan | 58% | 15.0 | 4.2 | 6.0 | 0.8 | 0.0 | 0.4 | 0.7 | 0.7 | 11.1 |
| AJ Johnson | 8% | 12.6 | 5.3 | 2.2 | 1.1 | 0.4 | 0.3 | 0.3 | 0.7 | 8.6 |
| Trendon Watford | 26% | 10.3 | 3.9 | 1.9 | 1.2 | 0.1 | 0.3 | 0.3 | 0.7 | 7.0 |
| Bryce McGowens | 52% | 9.8 | 3.4 | 1.2 | 0.7 | 0.2 | 0.4 | 0.1 | 0.3 | 5.2 |
| Julian Reese | 28% | 8.5 | 3.5 | 1.5 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 5.8 |

</details>


### MEM @ POR
Out: Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3PM under 2.5 | MEM @ POR | draftkings | 2.22 | 1.76 | 56.7% | 42.1% | 45.8% | +1.6% | +25.9% | 0.3% |
| Damian Lillard AST over 4.5 | MEM @ POR | draftkings | 2.20 | 1.80 | 55.5% | 42.5% | 45.7% | +0.6% | +22.1% | 0.1% |
| Jrue Holiday PRA over 20.5 | MEM @ POR | draftkings | 1.93 | 1.60 | 62.3% | 48.7% | 52.1% | +0.4% | +20.1% | 0.1% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Jrue Holiday 1+ 3pm **+** Deni Avdija 4+ ast | 53.4% | 1.87 | 1.96 | 1.65 | -11.9% |
| Deni Avdija 5+ reb **+** Damian Lillard 3+ ast **+** Jrue Holiday 1+ 3pm | 51.9% | 1.93 | 2.02 | 1.70 | -11.8% |
| Damian Lillard pts under 20.5 **+** Deni Avdija 3+ ast | 48.5% | 2.06 | 2.16 | 2.04 | -0.8% |
| Cedric Coward pts under 12.5 **+** Jrue Holiday 3+ ast | 40.5% | 2.47 | 2.59 | 2.50 | +1.3% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.2–119.5 | MEM 25% | 3.93 / 1.34 | POR -9.5 | 229.5 | POR -7.5 covers 55%; o233.5 42% |
| Expected (weighted by chance each plays) | 110.2–119.9 | MEM 24% | 4.19 / 1.31 | POR -9.5 | 230.5 | POR -7.5 covers 56%; o233.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| John Tonje (POR) | Questionable | 55% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |
| Jayson Kent (POR) | Questionable | 55% | 5.6 | 2.2 | 1.0 | 0.4 | 0.2 | 0.3 | 0.1 | 0.4 | 3.5 | small |
| Chris Youngblood (POR) | Questionable | 55% | 5.5 | 2.3 | 0.9 | 0.4 | 0.2 | 0.2 | 0.1 | 0.3 | 3.6 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 93% | 30.8 | 13.3 | 8.5 | 4.1 | 1.3 | 1.0 | 0.7 | 2.2 | 25.9 |
| Ty Jerome | 98% | 27.9 | 20.5 | 3.2 | 5.6 | 2.1 | 1.1 | 0.3 | 2.5 | 29.3 |
| Cedric Coward | 98% | 26.2 | 10.6 | 5.9 | 2.4 | 1.2 | 0.9 | 0.5 | 1.8 | 18.9 |
| Jaylen Wells | 98% | 25.3 | 9.9 | 2.9 | 1.4 | 1.3 | 1.0 | 0.1 | 1.1 | 14.2 |
| Jerami Grant | 98% | 22.1 | 9.5 | 2.4 | 1.5 | 1.0 | 0.8 | 0.7 | 1.5 | 13.4 |
| Zach Edey | 98% | 20.7 | 8.3 | 7.7 | 1.1 | 0.1 | 0.6 | 1.4 | 1.6 | 17.1 |
| Cam Spencer | 96% | 16.6 | 6.6 | 1.9 | 3.5 | 0.8 | 0.7 | 0.1 | 0.9 | 11.9 |
| Scotty Pippen Jr. | 97% | 15.3 | 7.2 | 2.1 | 2.8 | 0.6 | 1.2 | 0.3 | 1.5 | 12.1 |
| GG Jackson | 96% | 14.3 | 7.5 | 2.8 | 0.9 | 0.6 | 0.5 | 0.6 | 1.2 | 11.2 |
| Isaiah Stewart | 98% | 13.4 | 5.1 | 2.9 | 0.6 | 0.3 | 0.3 | 0.8 | 0.7 | 8.6 |
| Karim Lopez | 23% | 12.5 | 5.3 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.7 |
| Quinten Post | 88% | 11.9 | 3.9 | 2.2 | 0.6 | 0.3 | 0.3 | 0.3 | 0.7 | 6.7 |
| Olivier-Maxence Prosper | 30% | 11.7 | 6.1 | 2.3 | 0.6 | 0.5 | 0.6 | 0.2 | 0.7 | 9.0 |
| Javon Small | 35% | 9.7 | 4.1 | 1.5 | 1.4 | 0.4 | 0.5 | 0.1 | 0.8 | 7.0 |
| Carson Cooper | 35% | 8.6 | 3.7 | 1.6 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 6.0 |
| Kris Murray | 48% | 8.5 | 2.0 | 1.4 | 0.7 | 0.1 | 0.4 | 0.2 | 0.4 | 4.1 |
| Jahmai Mashack | 38% | 8.3 | 2.6 | 1.1 | 0.9 | 0.1 | 0.5 | 0.2 | 0.7 | 4.7 |
| Taylor Hendricks | 52% | 7.3 | 2.8 | 1.4 | 0.3 | 0.2 | 0.5 | 0.2 | 0.3 | 4.6 |

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
