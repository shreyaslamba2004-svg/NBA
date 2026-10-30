# NBA model · Thu 29 Oct 2026 (US date)

Updated **Fri 30 Oct, 01:10 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard AST over 5.5 | MEM @ POR | draftkings | 3.89 | 2.66 | 37.6% | 24.0% | 27.4% | +6.6% | +46.2% | 0.6% |
| Cedric Coward PTS under 12.5 | MEM @ POR | draftkings | 1.98 | 1.56 | 64.0% | 50.3% | 53.7% | +6.3% | +26.8% | 1.6% |

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Scoot Henderson 6+ pts | MEM @ POR | 58.7% | 1.70 | 1.79 | 1.59 | -6.8% |
| Damian Lillard 3+ ast **+** Deni Avdija 4+ ast | MEM @ POR | 60.1% | 1.66 | 1.75 | 1.54 | -7.3% |
| Damian Lillard 3+ ast **+** Toumani Camara 3+ reb | MEM @ POR | 57.8% | 1.73 | 1.82 | 1.60 | -7.3% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Scoot Henderson 6+ pts **+** Jrue Holiday 1+ 3pm | MEM @ POR | 49.7% | 2.01 | 2.11 | 1.81 | -10.2% |
| Damian Lillard 3+ ast **+** Scoot Henderson 6+ pts **+** Ja Morant 4+ ast | MEM @ POR | 49.2% | 2.03 | 2.13 | 1.82 | -10.4% |
| Scoot Henderson 6+ pts **+** Toumani Camara 3+ reb **+** Jrue Holiday 1+ 3pm | MEM @ POR | 48.9% | 2.05 | 2.15 | 1.83 | -10.7% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jrue Holiday 4+ ast **+** Deni Avdija 5+ reb | MEM @ POR | 47.7% | 2.10 | 2.20 | 2.04 | -2.6% |
| Jrue Holiday 4+ ast **+** Ja Morant 4+ ast | MEM @ POR | 49.9% | 2.01 | 2.11 | 1.95 | -2.8% |
| Jrue Holiday 4+ ast **+** Deni Avdija 4+ ast | MEM @ POR | 46.7% | 2.14 | 2.25 | 2.08 | -2.8% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Cedric Coward pts under 13.5 **+** Damian Lillard 3+ ast | MEM @ POR | 42.1% | 2.38 | 2.49 | 2.47 | +4.0% |
| Cedric Coward pts under 13.5 **+** Jrue Holiday 1+ 3pm | MEM @ POR | 46.6% | 2.15 | 2.25 | 2.23 | +3.9% |
| Cedric Coward pts under 13.5 **+** Scoot Henderson 6+ pts | MEM @ POR | 41.9% | 2.39 | 2.50 | 2.47 | +3.7% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 5.5 | MEM @ POR | draftkings | 4.00 | 2.32 | 43.1% | 23.4% | 28.3% | +13.2% | +72.4% | 1.1% |
| Cedric Coward PTS under 13.5 | MEM @ POR | sportsbet | 1.96 | 1.42 | 70.2% | 50.0% | 55.1% | +8.0% | +37.8% | 2.0% |
| Cameron Boozer PTS under 17.5 | MEM @ POR | tab | 1.90 | 1.34 | 74.4% | 50.7% | 56.6% | +7.7% | +41.4% | 2.0% |
| Jrue Holiday AST over 4.5 | MEM @ POR | draftkings | 2.49 | 1.71 | 58.4% | 37.5% | 42.8% | +6.4% | +45.4% | 1.1% |
| Ja Morant AST over 7.5 | MEM @ POR | draftkings | 3.31 | 2.30 | 43.4% | 28.2% | 32.0% | +6.0% | +43.7% | 0.7% |
| Cameron Boozer PTS under 16.5 | MEM @ POR | unibet | 1.92 | 1.44 | 69.6% | 50.0% | 54.9% | +5.3% | +33.4% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MEM @ POR | Fri 30 Oct 13:00 | 111.9–120.9 | MEM 26% | 3.84 / 1.35 | POR -9.5 | 232.5 | POR -7.5 covers 55%; o232.5 50% |

### MEM @ POR
Out: Shaedon Sharpe (POR), Robert Williams III (POR), Jahmai Mashack (MEM), Javon Small (MEM)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward PTS under 12.5 | MEM @ POR | draftkings | 1.98 | 1.56 | 64.0% | 50.3% | 53.7% | +6.3% | +26.8% | 1.6% |
| Ty Jerome PTS under 23.5 | MEM @ POR | tab | 1.95 | 1.61 | 62.1% | 49.3% | 52.5% | +2.5% | +21.3% | 0.7% |
| Jrue Holiday PTS over 12.5 | MEM @ POR | tab | 1.95 | 1.59 | 63.0% | 49.0% | 52.5% | +2.5% | +23.0% | 0.7% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Damian Lillard 3+ ast **+** Scoot Henderson 6+ pts | 58.7% | 1.70 | 1.79 | 1.59 | -6.8% |
| Damian Lillard 3+ ast **+** Scoot Henderson 6+ pts **+** Jrue Holiday 1+ 3pm | 49.7% | 2.01 | 2.11 | 1.81 | -10.2% |
| Jrue Holiday 4+ ast **+** Deni Avdija 5+ reb | 47.7% | 2.10 | 2.20 | 2.04 | -2.6% |
| Cedric Coward pts under 13.5 **+** Damian Lillard 3+ ast | 42.1% | 2.38 | 2.49 | 2.47 | +4.0% |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 93% | 31.5 | 14.0 | 8.7 | 3.9 | 1.4 | 1.1 | 0.7 | 2.1 | 26.6 |
| Ty Jerome | 98% | 28.9 | 21.9 | 3.3 | 6.3 | 2.2 | 1.2 | 0.3 | 2.5 | 31.4 |
| Cedric Coward | 98% | 27.5 | 11.3 | 6.5 | 2.8 | 1.3 | 0.9 | 0.6 | 1.9 | 20.5 |
| Jaylen Wells | 98% | 27.1 | 11.0 | 3.3 | 1.6 | 1.4 | 1.1 | 0.1 | 1.1 | 15.8 |
| Jerami Grant | 98% | 23.4 | 10.3 | 2.6 | 1.8 | 1.2 | 0.8 | 0.7 | 1.5 | 14.7 |
| Zach Edey | 98% | 21.5 | 8.3 | 8.2 | 1.2 | 0.1 | 0.6 | 1.5 | 1.6 | 17.7 |
| Cam Spencer | 96% | 17.9 | 6.8 | 2.1 | 4.0 | 0.9 | 0.7 | 0.1 | 1.0 | 12.9 |
| Scotty Pippen Jr. | 97% | 16.2 | 7.5 | 2.4 | 3.1 | 0.6 | 1.1 | 0.3 | 1.5 | 13.0 |
| GG Jackson | 96% | 15.4 | 7.7 | 3.1 | 1.1 | 0.7 | 0.5 | 0.6 | 1.2 | 11.9 |
| Isaiah Stewart | 98% | 14.4 | 5.5 | 3.2 | 0.7 | 0.3 | 0.3 | 0.9 | 0.7 | 9.5 |
| Quinten Post | 88% | 12.6 | 4.2 | 2.4 | 0.6 | 0.4 | 0.3 | 0.4 | 0.6 | 7.2 |
| Olivier-Maxence Prosper | 30% | 12.4 | 6.3 | 2.5 | 0.7 | 0.5 | 0.6 | 0.2 | 0.7 | 9.5 |
| Karim Lopez | 23% | 12.3 | 5.3 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.7 |
| Kris Murray | 48% | 9.5 | 2.3 | 1.6 | 0.8 | 0.1 | 0.4 | 0.2 | 0.4 | 4.6 |
| Taylor Hendricks | 52% | 8.2 | 2.9 | 1.7 | 0.4 | 0.2 | 0.5 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 97% | 34.3 | 23.9 | 7.9 | 6.3 | 1.9 | 0.9 | 0.7 | 3.8 | 38.2 |
| Damian Lillard | 98% | 31.9 | 18.5 | 4.4 | 5.0 | 2.6 | 1.2 | 0.3 | 2.3 | 27.9 |
| Jrue Holiday | 98% | 30.6 | 15.5 | 4.9 | 5.3 | 2.4 | 1.1 | 0.3 | 2.4 | 25.7 |
| Ja Morant | 98% | 30.2 | 19.2 | 3.8 | 7.3 | 1.4 | 1.3 | 0.3 | 2.9 | 30.2 |
| Toumani Camara | 98% | 29.9 | 12.0 | 4.8 | 1.9 | 2.0 | 1.2 | 0.5 | 1.3 | 18.7 |
| Donovan Clingan | 98% | 26.2 | 11.2 | 11.5 | 2.0 | 1.1 | 0.7 | 2.1 | 1.3 | 24.7 |
| Sidy Cissoko | 93% | 22.6 | 6.2 | 3.2 | 1.8 | 0.7 | 1.1 | 0.4 | 1.1 | 11.3 |
| Scoot Henderson | 98% | 22.4 | 10.9 | 2.3 | 2.8 | 1.4 | 1.0 | 0.2 | 2.0 | 16.1 |
| Micah Potter | 52% | 14.4 | 6.1 | 4.1 | 0.9 | 0.6 | 0.4 | 0.3 | 0.9 | 11.1 |
| Vit Krejci | 96% | 11.9 | 4.1 | 1.7 | 1.0 | 0.6 | 0.5 | 0.2 | 0.4 | 6.8 |
| Branden Carlson | 16% | 8.7 | 3.6 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 |
| John Tonje | 16% | 8.7 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Yang Hansen | 52% | 8.1 | 2.7 | 2.1 | 0.5 | 0.1 | 0.2 | 0.3 | 0.8 | 5.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-29/`._
