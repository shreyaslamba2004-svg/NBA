# NBA model · Thu 29 Oct 2026 (US date)

Updated **Fri 30 Oct, 10:30 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kingston Flemings PTS under 8.5 | CLE @ ATL | tab | 2.00 | 1.59 | 63.0% | 50.6% | 53.8% | +7.5% | +26.1% | 1.9% |
| Damian Lillard AST over 5.5 | MEM @ POR | draftkings | 3.82 | 2.63 | 38.0% | 24.5% | 27.9% | +6.4% | +45.2% | 0.6% |
| Ja Morant AST over 7.5 | MEM @ POR | draftkings | 3.26 | 2.31 | 43.3% | 28.7% | 32.3% | +5.4% | +41.1% | 0.6% |

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast | MEM @ POR | 60.8% | 1.64 | 1.73 | 1.53 | -7.2% |
| Damian Lillard 3+ ast **+** Toumani Camara 3+ reb | MEM @ POR | 58.2% | 1.72 | 1.80 | 1.59 | -7.4% |
| Damian Lillard 3+ ast **+** Deni Avdija 5+ reb | MEM @ POR | 61.2% | 1.63 | 1.72 | 1.51 | -7.5% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Derik Queen 8+ pts **+** Trey Murphy III 2+ 3pm **+** Precious Achiuwa 6+ pts | SAC @ NOP | 51.4% | 1.94 | 2.04 | 1.78 | -8.6% |
| Derik Queen 8+ pts **+** Trey Murphy III 2+ 3pm **+** Domantas Sabonis 25+ pra | SAC @ NOP | 52.0% | 1.92 | 2.02 | 1.74 | -9.4% |
| Derik Queen 8+ pts **+** Trey Murphy III 2+ 3pm **+** Zion Williamson 3+ reb | SAC @ NOP | 51.6% | 1.94 | 2.03 | 1.75 | -9.5% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Kingston Flemings pts under 8.5 **+** Evan Mobley 4+ reb | CLE @ ATL | 49.4% | 2.02 | 2.12 | 2.06 | +1.7% |
| Damian Lillard pts under 21.5 **+** Jrue Holiday 1+ 3pm | MEM @ POR | 47.6% | 2.10 | 2.20 | 2.07 | -1.3% |
| Derik Queen 23+ pra **+** Domantas Sabonis 25+ pra | SAC @ NOP | 47.0% | 2.13 | 2.24 | 2.10 | -1.6% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Kingston Flemings pts under 8.5 **+** Donovan Mitchell 20+ pra | CLE @ ATL | 48.0% | 2.08 | 2.19 | 2.14 | +2.6% |
| Kingston Flemings pts under 8.5 **+** Donovan Mitchell 3+ reb | CLE @ ATL | 42.6% | 2.35 | 2.47 | 2.41 | +2.5% |
| Kingston Flemings pts under 8.5 **+** Donovan Mitchell 12+ pts | CLE @ ATL | 48.5% | 2.06 | 2.16 | 2.11 | +2.5% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 5.5 | MEM @ POR | draftkings | 3.99 | 2.29 | 43.6% | 23.4% | 28.5% | +13.6% | +74.0% | 1.1% |
| Derik Queen REB over 9.5 | SAC @ NOP | draftkings | 3.59 | 2.40 | 41.6% | 26.0% | 29.9% | +7.5% | +49.5% | 0.7% |
| Precious Achiuwa PTS over 14.5 | SAC @ NOP | draftkings | 3.58 | 2.40 | 41.7% | 26.1% | 30.0% | +7.4% | +49.2% | 0.7% |
| Jrue Holiday AST over 4.5 | MEM @ POR | draftkings | 2.49 | 1.70 | 58.9% | 37.5% | 42.9% | +6.8% | +46.8% | 1.1% |
| Derik Queen PR over 19.5 | SAC @ NOP | draftkings | 2.00 | 1.53 | 65.6% | 48.5% | 52.8% | +5.6% | +31.1% | 1.4% |
| Jrue Holiday REB over 4.5 | MEM @ POR | draftkings | 2.72 | 1.93 | 51.8% | 34.4% | 38.7% | +5.3% | +40.9% | 0.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CLE @ ATL | Fri 30 Oct 11:00 | 116.7–117.1 | CLE 48% | 2.06 / 1.94 | ATL +0.5 | 233.5 | ATL -1.5 covers 48%; o237.5 42% |
| SAC @ NOP | Fri 30 Oct 11:00 | 116.0–121.2 | SAC 36% | 2.80 / 1.56 | NOP -5.5 | 237.5 | NOP -6.5 covers 46%; o235.5 54% |
| MEM @ POR | Fri 30 Oct 13:00 | 111.0–119.3 | MEM 28% | 3.61 / 1.38 | POR -8.5 | 230.5 | POR -7.5 covers 53%; o232.5 45% |

### CLE @ ATL
Out: RayJ Dennis (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Jalen Wilson (ATL), Tristan Enaruna (CLE), Meleek Thomas (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kingston Flemings PTS under 8.5 | CLE @ ATL | tab | 2.00 | 1.59 | 63.0% | 50.6% | 53.8% | +7.5% | +26.1% | 1.9% |
| Jalen Johnson PTS under 22.5 | CLE @ ATL | unibet | 1.91 | 1.59 | 63.0% | 51.1% | 54.1% | +3.2% | +20.3% | 0.9% |
| Sam Merrill PTS under 8.5 | CLE @ ATL | tab | 1.95 | 1.73 | 57.7% | 51.0% | 52.7% | +2.9% | +12.7% | 0.8% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Donovan Mitchell 3+ reb **+** Onyeka Okongwu 8+ pts | 60.7% | 1.65 | 1.73 | 1.52 | -7.8% |
| Kingston Flemings pts under 8.5 **+** Evan Mobley 4+ reb | 49.4% | 2.02 | 2.12 | 2.06 | +1.7% |
| Kingston Flemings pts under 8.5 **+** Donovan Mitchell 20+ pra | 48.0% | 2.08 | 2.19 | 2.14 | +2.6% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 98% | 35.3 | 26.1 | 5.1 | 4.5 | 2.8 | 1.4 | 0.4 | 3.0 | 35.7 |
| James Harden | 98% | 35.1 | 18.3 | 4.5 | 6.0 | 2.2 | 1.3 | 0.5 | 3.7 | 28.8 |
| Evan Mobley | 98% | 34.0 | 18.0 | 9.0 | 3.3 | 1.4 | 1.0 | 1.6 | 2.1 | 30.3 |
| Peyton Watson | 98% | 31.6 | 14.8 | 4.6 | 2.1 | 1.3 | 1.0 | 1.1 | 2.2 | 21.5 |
| Jarrett Allen | 98% | 28.7 | 13.3 | 8.6 | 1.5 | 0.0 | 1.0 | 1.4 | 1.4 | 23.4 |
| Sam Merrill | 98% | 23.8 | 8.3 | 2.2 | 1.6 | 1.4 | 0.7 | 0.1 | 0.7 | 12.1 |
| Jaylon Tyson | 96% | 21.7 | 8.7 | 3.8 | 1.9 | 1.1 | 0.6 | 0.3 | 1.2 | 14.3 |
| Mario Hezonja | 93% | 16.4 | 6.2 | 3.2 | 0.9 | 0.6 | 0.5 | 0.3 | 0.8 | 10.3 |
| Craig Porter Jr. | 52% | 10.3 | 2.9 | 1.9 | 1.6 | 0.1 | 0.5 | 0.3 | 0.8 | 6.3 |
| Tyrese Proctor | 64% | 9.9 | 4.6 | 1.3 | 1.3 | 0.5 | 0.5 | 0.1 | 0.8 | 7.1 |
| Thomas Bryant | 30% | 9.7 | 4.5 | 2.6 | 0.5 | 0.4 | 0.2 | 0.3 | 0.4 | 7.6 |
| Ernest Udeh Jr. | 16% | 8.7 | 3.7 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.1 |
| Riley Minix | 23% | 7.9 | 3.1 | 1.0 | 0.5 | 0.2 | 0.2 | 0.1 | 0.3 | 4.5 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 35.1 | 20.8 | 9.0 | 7.2 | 1.6 | 1.2 | 0.5 | 3.0 | 37.0 |
| Nickeil Alexander-Walker | 98% | 32.7 | 19.0 | 3.0 | 3.1 | 3.1 | 1.2 | 0.5 | 2.1 | 25.2 |
| Dyson Daniels | 98% | 30.3 | 11.2 | 6.0 | 4.7 | 0.6 | 2.2 | 0.3 | 1.6 | 21.9 |
| Onyeka Okongwu | 98% | 30.2 | 12.6 | 6.7 | 2.6 | 1.5 | 1.1 | 0.9 | 1.3 | 21.9 |
| CJ McCollum | 98% | 28.3 | 17.0 | 2.6 | 3.0 | 2.2 | 0.9 | 0.5 | 1.8 | 22.6 |
| Aaron Wiggins | 91% | 26.0 | 11.4 | 3.2 | 1.7 | 1.7 | 1.0 | 0.3 | 1.0 | 16.3 |
| Luguentz Dort | 98% | 22.8 | 7.9 | 2.8 | 1.4 | 1.2 | 0.8 | 0.2 | 0.7 | 12.0 |
| Kingston Flemings | 96% | 21.2 | 7.7 | 3.2 | 3.9 | 0.7 | 0.6 | 0.3 | 1.6 | 14.8 |
| Jock Landale | 98% | 18.0 | 7.7 | 4.3 | 1.5 | 0.6 | 0.5 | 0.5 | 0.8 | 13.5 |
| Corey Kispert | 52% | 9.0 | 4.5 | 1.2 | 0.7 | 0.5 | 0.2 | 0.1 | 0.4 | 6.4 |
| Asa Newell | 52% | 7.9 | 3.3 | 1.6 | 0.4 | 0.2 | 0.3 | 0.2 | 0.3 | 5.3 |
| Dorian Finney-Smith | 52% | 7.3 | 2.1 | 1.1 | 0.4 | 0.1 | 0.2 | 0.1 | 0.3 | 3.6 |
| Zuby Ejiofor | 52% | 6.1 | 2.5 | 1.1 | 0.5 | 0.2 | 0.2 | 0.1 | 0.3 | 4.1 |

</details>


### SAC @ NOP
Out: Yves Missi (NOP), Dejounte Murray (NOP), Jordan Poole (NOP), Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PTS over 11.5 | SAC @ NOP | sportsbet | 1.92 | 1.58 | 63.1% | 49.6% | 53.0% | +1.6% | +21.1% | 0.4% |
| De'Andre Hunter PTS under 12.5 | SAC @ NOP | tab | 1.85 | 1.65 | 60.5% | 52.1% | 54.2% | +0.2% | +11.8% | 0.1% |
| Derik Queen RA over 10.5 | SAC @ NOP | draftkings | 1.81 | 1.51 | 66.1% | 51.8% | 55.4% | +0.1% | +19.4% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Derik Queen 8+ pts **+** Precious Achiuwa 6+ pts **+** Trey Murphy III 20+ pra | 55.0% | 1.82 | 1.91 | 1.65 | -9.4% |
| Derik Queen 8+ pts **+** Trey Murphy III 2+ 3pm **+** Precious Achiuwa 6+ pts | 51.4% | 1.94 | 2.04 | 1.78 | -8.6% |
| Derik Queen 23+ pra **+** Domantas Sabonis 25+ pra | 47.0% | 2.13 | 2.24 | 2.10 | -1.6% |
| Precious Achiuwa 11+ pts **+** Derik Queen 8+ pts | 42.4% | 2.36 | 2.48 | 2.40 | +1.7% |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 93% | 34.8 | 20.9 | 3.9 | 4.7 | 2.1 | 1.1 | 0.4 | 2.8 | 29.5 |
| Domantas Sabonis | 98% | 34.5 | 18.8 | 14.4 | 5.9 | 0.4 | 1.0 | 0.4 | 2.6 | 39.1 |
| Zach LaVine | 98% | 34.4 | 21.9 | 3.5 | 2.9 | 2.8 | 0.9 | 0.3 | 2.3 | 28.4 |
| Precious Achiuwa | 98% | 29.7 | 14.0 | 8.2 | 1.7 | 0.4 | 1.1 | 1.0 | 1.3 | 23.9 |
| De'Andre Hunter | 98% | 27.8 | 11.8 | 5.2 | 1.6 | 1.6 | 0.7 | 0.2 | 1.2 | 18.5 |
| Daeqwon Plowden | 98% | 18.2 | 5.9 | 2.1 | 0.9 | 0.9 | 0.5 | 0.2 | 0.6 | 8.9 |
| Jonathan Mogbo | 64% | 16.0 | 5.6 | 2.9 | 0.9 | 0.5 | 0.5 | 0.3 | 0.7 | 9.4 |
| Malik Monk | 96% | 15.6 | 8.1 | 1.6 | 2.7 | 1.0 | 0.5 | 0.3 | 1.1 | 12.4 |
| Emanuel Sharp | 93% | 15.4 | 4.9 | 1.0 | 1.0 | 0.6 | 0.5 | 0.2 | 0.6 | 7.0 |
| Nique Clifford | 72% | 12.5 | 4.9 | 1.9 | 1.2 | 0.4 | 0.5 | 0.2 | 0.9 | 8.0 |
| Leaky Black | 52% | 11.4 | 3.1 | 2.2 | 0.8 | 0.3 | 0.5 | 0.4 | 0.4 | 6.1 |
| Alex Karaban | 58% | 9.3 | 2.5 | 1.8 | 0.6 | 0.0 | 0.3 | 0.3 | 0.5 | 5.0 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 35.4 | 20.8 | 5.6 | 4.0 | 3.4 | 1.4 | 0.5 | 1.9 | 30.4 |
| Zion Williamson | 96% | 33.6 | 24.5 | 6.0 | 3.8 | 0.2 | 1.3 | 0.7 | 2.4 | 34.4 |
| Saddiq Bey | 96% | 30.5 | 18.1 | 5.0 | 2.7 | 2.4 | 0.9 | 0.2 | 1.2 | 25.8 |
| Jeremiah Fears | 98% | 29.7 | 17.8 | 4.1 | 4.2 | 1.6 | 1.3 | 0.4 | 2.5 | 26.0 |
| Derik Queen | 98% | 28.7 | 14.4 | 9.0 | 3.6 | 0.4 | 1.2 | 1.1 | 2.5 | 27.1 |
| Herbert Jones | 96% | 23.8 | 7.2 | 2.8 | 2.0 | 1.0 | 1.4 | 0.4 | 1.0 | 12.0 |
| Bennedict Mathurin | 98% | 21.6 | 11.1 | 3.9 | 2.1 | 0.8 | 0.6 | 0.2 | 1.5 | 17.2 |
| Karlo Matkovic | 86% | 18.5 | 6.9 | 4.6 | 1.1 | 0.6 | 0.6 | 1.1 | 0.7 | 12.5 |
| DeAndre Jordan | 58% | 18.1 | 5.0 | 7.3 | 1.0 | 0.0 | 0.4 | 0.9 | 0.9 | 13.2 |
| Trendon Watford | 26% | 13.5 | 5.3 | 2.5 | 1.7 | 0.1 | 0.4 | 0.4 | 1.0 | 9.6 |
| Bryce McGowens | 52% | 12.9 | 4.5 | 1.5 | 0.9 | 0.4 | 0.5 | 0.2 | 0.5 | 7.0 |
| AJ Johnson | 8% | 12.3 | 5.1 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.3 |
| Julian Reese | 30% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 |

</details>


### MEM @ POR
Out: Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3PM under 2.5 | MEM @ POR | draftkings | 2.24 | 1.81 | 55.2% | 41.7% | 45.1% | +1.0% | +23.6% | 0.2% |
| Cameron Boozer PRA under 28.5 | MEM @ POR | draftkings | 1.86 | 1.54 | 64.9% | 50.2% | 53.9% | +0.3% | +20.9% | 0.1% |
| Cedric Coward PR under 18.5 | MEM @ POR | draftkings | 1.81 | 1.51 | 66.2% | 51.5% | 55.2% | +0.1% | +20.0% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast | 60.8% | 1.64 | 1.73 | 1.53 | -7.2% |
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast **+** Ja Morant 4+ ast | 51.0% | 1.96 | 2.06 | 1.75 | -10.8% |
| Damian Lillard pts under 21.5 **+** Jrue Holiday 1+ 3pm | 47.6% | 2.10 | 2.20 | 2.07 | -1.3% |
| Jrue Holiday 8+ ra **+** Damian Lillard 3+ ast | 43.3% | 2.31 | 2.43 | 2.35 | +1.6% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.0–119.3 | MEM 28% | 3.61 / 1.38 | POR -8.5 | 230.5 | POR -7.5 covers 53%; o232.5 45% |
| Expected (weighted by chance each plays) | 110.5–119.8 | MEM 25% | 4.04 / 1.33 | POR -9.5 | 230.5 | POR -7.5 covers 55%; o232.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Robert Williams III (POR) | Doubtful | 20% | 18.5 | 7.8 | 8.1 | 1.1 | 0.2 | 0.6 | 1.5 | 1.0 | 17.0 | small |
| John Tonje (POR) | Questionable | 55% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |
| Jayson Kent (POR) | Questionable | 55% | 6.6 | 2.4 | 1.1 | 0.5 | 0.2 | 0.3 | 0.1 | 0.4 | 4.0 | small |
| Chris Youngblood (POR) | Questionable | 55% | 6.8 | 2.6 | 1.1 | 0.5 | 0.3 | 0.2 | 0.1 | 0.4 | 4.2 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 93% | 30.8 | 13.4 | 8.6 | 4.1 | 1.3 | 1.0 | 0.7 | 2.2 | 26.0 |
| Ty Jerome | 98% | 28.0 | 20.8 | 3.2 | 5.7 | 2.1 | 1.2 | 0.3 | 2.5 | 29.6 |
| Cedric Coward | 98% | 26.2 | 10.6 | 6.0 | 2.4 | 1.2 | 0.9 | 0.5 | 1.8 | 19.0 |
| Jaylen Wells | 98% | 25.3 | 10.0 | 2.9 | 1.4 | 1.3 | 1.0 | 0.1 | 1.1 | 14.3 |
| Jerami Grant | 98% | 22.2 | 9.6 | 2.4 | 1.5 | 1.0 | 0.8 | 0.7 | 1.5 | 13.5 |
| Zach Edey | 98% | 20.7 | 8.3 | 7.8 | 1.1 | 0.1 | 0.6 | 1.4 | 1.6 | 17.2 |
| Cam Spencer | 96% | 16.6 | 6.6 | 1.9 | 3.5 | 0.8 | 0.7 | 0.1 | 0.9 | 12.0 |
| Scotty Pippen Jr. | 97% | 15.4 | 7.2 | 2.1 | 2.8 | 0.6 | 1.2 | 0.3 | 1.5 | 12.1 |
| GG Jackson | 96% | 14.3 | 7.5 | 2.8 | 0.9 | 0.6 | 0.5 | 0.6 | 1.2 | 11.2 |
| Isaiah Stewart | 98% | 13.3 | 5.0 | 2.9 | 0.6 | 0.3 | 0.3 | 0.8 | 0.7 | 8.6 |
| Karim Lopez | 23% | 12.4 | 5.4 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.7 |
| Quinten Post | 88% | 11.9 | 3.9 | 2.2 | 0.6 | 0.3 | 0.3 | 0.3 | 0.6 | 6.6 |
| Olivier-Maxence Prosper | 30% | 11.9 | 6.2 | 2.4 | 0.6 | 0.5 | 0.6 | 0.2 | 0.7 | 9.2 |
| Javon Small | 35% | 9.7 | 4.2 | 1.5 | 1.4 | 0.4 | 0.5 | 0.1 | 0.8 | 7.1 |
| Carson Cooper | 35% | 8.6 | 3.7 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Kris Murray | 48% | 8.4 | 2.0 | 1.4 | 0.6 | 0.1 | 0.4 | 0.2 | 0.4 | 4.0 |
| Jahmai Mashack | 38% | 8.3 | 2.6 | 1.1 | 0.9 | 0.1 | 0.5 | 0.2 | 0.7 | 4.7 |
| Taylor Hendricks | 52% | 7.5 | 2.9 | 1.5 | 0.3 | 0.2 | 0.5 | 0.2 | 0.4 | 4.7 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 97% | 34.3 | 23.8 | 7.9 | 6.3 | 1.9 | 0.9 | 0.7 | 3.8 | 38.0 |
| Damian Lillard | 98% | 31.9 | 18.4 | 4.4 | 5.0 | 2.5 | 1.2 | 0.3 | 2.3 | 27.8 |
| Jrue Holiday | 98% | 30.7 | 15.4 | 5.0 | 5.3 | 2.4 | 1.2 | 0.3 | 2.4 | 25.7 |
| Ja Morant | 98% | 30.1 | 19.1 | 3.8 | 7.2 | 1.4 | 1.3 | 0.3 | 2.9 | 30.1 |
| Toumani Camara | 98% | 29.8 | 11.9 | 4.7 | 1.9 | 2.0 | 1.2 | 0.5 | 1.3 | 18.5 |
| Donovan Clingan | 98% | 26.2 | 11.2 | 11.5 | 2.0 | 1.1 | 0.7 | 2.1 | 1.3 | 24.7 |
| Sidy Cissoko | 93% | 22.7 | 6.2 | 3.3 | 1.9 | 0.7 | 1.1 | 0.4 | 1.1 | 11.4 |
| Scoot Henderson | 98% | 22.3 | 10.8 | 2.3 | 2.8 | 1.4 | 1.0 | 0.2 | 2.0 | 15.9 |
| Micah Potter | 52% | 14.4 | 6.0 | 4.0 | 0.9 | 0.6 | 0.4 | 0.3 | 0.8 | 10.9 |
| Vit Krejci | 96% | 11.9 | 4.1 | 1.7 | 1.0 | 0.6 | 0.5 | 0.2 | 0.4 | 6.8 |
| Branden Carlson | 16% | 8.8 | 3.7 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.5 | 6.1 |
| Yang Hansen | 52% | 8.1 | 2.7 | 2.0 | 0.5 | 0.1 | 0.2 | 0.3 | 0.8 | 5.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-29/`._
