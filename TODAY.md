# NBA model · Thu 29 Oct 2026 (US date)

Updated **Fri 30 Oct, 11:16 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard AST over 5.5 | MEM @ POR | draftkings | 3.91 | 2.63 | 38.0% | 23.9% | 27.4% | +7.2% | +48.6% | 0.6% |
| Ja Morant AST over 7.5 | MEM @ POR | draftkings | 3.29 | 2.31 | 43.3% | 28.4% | 32.1% | +5.7% | +42.4% | 0.6% |

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast | MEM @ POR | 60.8% | 1.64 | 1.73 | 1.53 | -7.2% |
| Damian Lillard 3+ ast **+** Toumani Camara 3+ reb | MEM @ POR | 58.3% | 1.71 | 1.80 | 1.59 | -7.5% |
| Damian Lillard 3+ ast **+** Deni Avdija 5+ reb | MEM @ POR | 61.3% | 1.63 | 1.71 | 1.51 | -7.6% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast **+** Ja Morant 4+ ast | MEM @ POR | 51.2% | 1.95 | 2.05 | 1.74 | -10.9% |
| Damian Lillard 3+ ast **+** Jrue Holiday 1+ 3pm **+** Scoot Henderson 6+ pts | MEM @ POR | 48.8% | 2.05 | 2.15 | 1.82 | -11.0% |
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast **+** Jrue Holiday 1+ 3pm | MEM @ POR | 50.9% | 1.96 | 2.06 | 1.75 | -11.1% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jrue Holiday 8+ ra **+** Ja Morant 4+ ast | MEM @ POR | 47.5% | 2.10 | 2.21 | 2.09 | -0.7% |
| Ty Jerome pts under 24.5 **+** Jrue Holiday 1+ 3pm | MEM @ POR | 47.2% | 2.12 | 2.22 | 2.08 | -2.0% |
| Ty Jerome pa under 30.5 **+** Jrue Holiday 1+ 3pm | MEM @ POR | 47.0% | 2.13 | 2.23 | 2.08 | -2.0% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jrue Holiday 8+ ra **+** Damian Lillard 3+ ast | MEM @ POR | 44.0% | 2.27 | 2.39 | 2.30 | +1.0% |
| Jrue Holiday 8+ ra **+** Scoot Henderson 6+ pts | MEM @ POR | 43.1% | 2.32 | 2.43 | 2.33 | +0.6% |
| Damian Lillard pts under 20.5 **+** Jrue Holiday 3+ ast | MEM @ POR | 40.6% | 2.46 | 2.59 | 2.47 | +0.4% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 4.5 | MEM @ POR | draftkings | 2.45 | 1.70 | 58.9% | 38.1% | 43.3% | +6.2% | +44.4% | 1.1% |
| Jrue Holiday REB over 4.5 | MEM @ POR | draftkings | 2.73 | 1.93 | 51.8% | 34.2% | 38.6% | +5.4% | +41.4% | 0.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MEM @ POR | Fri 30 Oct 13:00 | 111.0–119.3 | MEM 28% | 3.61 / 1.38 | POR -8.5 | 230.5 | POR -7.5 covers 53%; o232.5 45% |

### MEM @ POR
Out: Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3PM under 2.5 | MEM @ POR | draftkings | 2.24 | 1.81 | 55.2% | 41.7% | 45.1% | +1.0% | +23.6% | 0.2% |
| Cameron Boozer PR under 23.5 | MEM @ POR | draftkings | 1.95 | 1.62 | 61.9% | 47.9% | 51.4% | +0.3% | +20.8% | 0.1% |
| Isaiah Stewart REB under 3.5 | MEM @ POR | draftkings | 1.80 | 1.50 | 66.7% | 51.9% | 55.6% | +0.1% | +20.0% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast | 60.8% | 1.64 | 1.73 | 1.53 | -7.2% |
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast **+** Ja Morant 4+ ast | 51.2% | 1.95 | 2.05 | 1.74 | -10.9% |
| Jrue Holiday 8+ ra **+** Ja Morant 4+ ast | 47.5% | 2.10 | 2.21 | 2.09 | -0.7% |
| Jrue Holiday 8+ ra **+** Damian Lillard 3+ ast | 44.0% | 2.27 | 2.39 | 2.30 | +1.0% |

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
