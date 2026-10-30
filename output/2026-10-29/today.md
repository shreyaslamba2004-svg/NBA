# NBA model · Thu 29 Oct 2026 (US date)

Updated **Fri 30 Oct, 12:26 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price, and use the Fair column as your minimum odds.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard AST over 5.5 | MEM @ POR | draftkings | 3.81 | 2.65 | 37.7% | 24.5% | 27.8% | +6.0% | +43.7% | 0.5% |

## Best same-game multis by price (1.50 to 2.50)

**Price 1.50-1.65**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Cedric Coward 4+ reb **+** Toumani Camara 3+ reb | MEM @ POR | 61.1% | 1.64 | 1.72 | 1.51 | -7.8% |
| Deni Avdija 5+ reb **+** Toumani Camara 3+ reb | MEM @ POR | 60.7% | 1.65 | 1.73 | 1.51 | -8.2% |
| Toumani Camara 3+ reb **+** Deni Avdija 4+ ast | MEM @ POR | 59.7% | 1.67 | 1.76 | 1.53 | -8.3% |

**Price 1.65-1.85**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Scoot Henderson 6+ pts **+** Jrue Holiday 1+ 3pm **+** Toumani Camara 3+ reb | MEM @ POR | 49.3% | 2.03 | 2.13 | 1.81 | -10.9% |
| Scoot Henderson 6+ pts **+** Jrue Holiday 1+ 3pm **+** Cedric Coward 4+ reb | MEM @ POR | 51.7% | 1.93 | 2.03 | 1.72 | -11.0% |
| Scoot Henderson 6+ pts **+** Jrue Holiday 1+ 3pm **+** Deni Avdija 4+ ast | MEM @ POR | 50.8% | 1.97 | 2.07 | 1.75 | -11.1% |

**Price 1.85-2.10**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jrue Holiday 8+ ra **+** Ja Morant 4+ ast | MEM @ POR | 47.8% | 2.09 | 2.20 | 2.10 | +0.2% |
| Jrue Holiday 4+ ast **+** Deni Avdija 5+ reb | MEM @ POR | 47.9% | 2.09 | 2.19 | 2.04 | -2.0% |
| Jrue Holiday 4+ ast **+** Cedric Coward 4+ reb | MEM @ POR | 47.9% | 2.09 | 2.19 | 2.04 | -2.4% |

**Price 2.10-2.50**

| Legs | Game | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|--:|
| Jrue Holiday 8+ ra **+** Damian Lillard 3+ ast | MEM @ POR | 44.1% | 2.27 | 2.38 | 2.30 | +1.4% |
| Jrue Holiday 21+ pra **+** Damian Lillard 3+ ast | MEM @ POR | 42.5% | 2.35 | 2.47 | 2.37 | +0.9% |
| Jrue Holiday 8+ ra **+** Scoot Henderson 6+ pts | MEM @ POR | 43.6% | 2.29 | 2.41 | 2.31 | +0.9% |

Bookies price multis with their own correlation model, so compare their quoted price with **Take at ≥**: a multi is only value at that price or better, and a negative EV here means the legs multiplied fall short of it. "10+ pts" means 10 or more. Each game's section below has its own best multis.

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Cam Spencer AST over 4.5 | MEM @ POR | draftkings | 3.82 | Ty Jerome | 45.6% | 37.5% | +9.4% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 5.5 | MEM @ POR | draftkings | 3.99 | 2.30 | 43.5% | 23.4% | 28.4% | +13.5% | +73.8% | 1.1% |
| Jrue Holiday AST over 4.5 | MEM @ POR | draftkings | 2.50 | 1.70 | 58.8% | 37.4% | 42.8% | +6.9% | +47.1% | 1.1% |
| Ja Morant AST over 7.5 | MEM @ POR | draftkings | 3.34 | 2.30 | 43.5% | 28.0% | 31.9% | +6.4% | +45.2% | 0.7% |
| Jrue Holiday REB over 4.5 | MEM @ POR | draftkings | 2.67 | 1.88 | 53.1% | 35.0% | 39.5% | +5.5% | +41.8% | 0.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MEM @ POR | Fri 30 Oct 13:00 | 111.5–121.4 | MEM 24% | 4.17 / 1.32 | POR -9.5 | 232.5 | POR -7.5 covers 57%; o232.5 51% |

### MEM @ POR
Out: Shaedon Sharpe (POR), Robert Williams III (POR), Jahmai Mashack (MEM), Javon Small (MEM)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday PTS over 12.5 | MEM @ POR | tab | 1.95 | 1.60 | 62.4% | 49.0% | 52.3% | +2.2% | +21.8% | 0.6% |
| Scoot Henderson PTS over 8.5 | MEM @ POR | tab | 1.90 | 1.60 | 62.5% | 50.0% | 53.1% | +1.0% | +18.8% | 0.3% |
| Damian Lillard 3PM under 2.5 | MEM @ POR | draftkings | 2.28 | 1.89 | 52.8% | 41.0% | 43.9% | +0.2% | +20.3% | 0.0% |

**Best multis (one per price band)**

| Legs | Chance | Fair | Take at ≥ | Legs multiplied | EV if multiplied |
|---|--:|--:|--:|--:|--:|
| Cedric Coward 4+ reb **+** Toumani Camara 3+ reb | 61.1% | 1.64 | 1.72 | 1.51 | -7.8% |
| Scoot Henderson 6+ pts **+** Jrue Holiday 1+ 3pm **+** Toumani Camara 3+ reb | 49.3% | 2.03 | 2.13 | 1.81 | -10.9% |
| Jrue Holiday 8+ ra **+** Ja Morant 4+ ast | 47.8% | 2.09 | 2.20 | 2.10 | +0.2% |
| Jrue Holiday 8+ ra **+** Damian Lillard 3+ ast | 44.1% | 2.27 | 2.38 | 2.30 | +1.4% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.5–121.4 | MEM 24% | 4.17 / 1.32 | POR -9.5 | 232.5 | POR -7.5 covers 57%; o232.5 51% |
| Expected (weighted by chance each plays) | 111.7–121.1 | MEM 25% | 4.03 / 1.33 | POR -9.5 | 232.5 | POR -7.5 covers 56%; o232.5 50% |
| if Ty Jerome plays | 111.9–120.9 | MEM 26% | 3.84 / 1.35 | POR -9.5 | 232.5 | POR -7.5 covers 55%; o232.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ty Jerome (MEM) | Questionable | 55% | 28.9 | 21.9 | 3.3 | 6.3 | 2.2 | 1.2 | 0.3 | 2.5 | 31.4 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 93% | 33.5 | 16.5 | 9.5 | 4.4 | 1.6 | 1.2 | 0.8 | 2.5 | 30.4 |
| Cedric Coward | 98% | 30.0 | 13.9 | 7.2 | 3.2 | 1.6 | 1.1 | 0.6 | 2.3 | 24.3 |
| Jaylen Wells | 98% | 29.5 | 13.3 | 3.5 | 1.9 | 1.8 | 1.2 | 0.2 | 1.4 | 18.7 |
| Jerami Grant | 98% | 25.7 | 12.8 | 2.9 | 2.0 | 1.4 | 0.9 | 0.8 | 1.8 | 17.7 |
| Zach Edey | 98% | 23.9 | 9.8 | 9.2 | 1.3 | 0.1 | 0.6 | 1.6 | 1.8 | 20.3 |
| Cam Spencer | 96% | 19.7 | 8.4 | 2.3 | 4.5 | 1.1 | 0.8 | 0.2 | 1.1 | 15.2 |
| Scotty Pippen Jr. | 97% | 19.1 | 9.5 | 2.8 | 3.6 | 0.8 | 1.3 | 0.4 | 1.9 | 16.0 |
| Isaiah Stewart | 98% | 16.7 | 6.7 | 3.8 | 0.8 | 0.4 | 0.3 | 1.0 | 0.8 | 11.4 |
| GG Jackson | 96% | 16.6 | 9.2 | 3.4 | 1.2 | 0.8 | 0.5 | 0.7 | 1.4 | 13.8 |
| Quinten Post | 88% | 16.0 | 5.4 | 3.0 | 0.8 | 0.5 | 0.4 | 0.5 | 0.8 | 9.1 |
| Olivier-Maxence Prosper | 30% | 14.3 | 7.9 | 2.9 | 0.8 | 0.6 | 0.8 | 0.2 | 0.8 | 11.5 |
| Karim Lopez | 23% | 12.4 | 5.4 | 2.2 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.8 |
| Kris Murray | 48% | 11.7 | 3.0 | 2.0 | 0.9 | 0.2 | 0.5 | 0.2 | 0.5 | 5.9 |
| Taylor Hendricks | 52% | 9.6 | 3.6 | 1.9 | 0.5 | 0.3 | 0.6 | 0.3 | 0.5 | 6.0 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 97% | 34.2 | 24.0 | 7.9 | 6.3 | 1.9 | 0.9 | 0.7 | 3.8 | 38.2 |
| Damian Lillard | 98% | 32.0 | 18.6 | 4.4 | 5.0 | 2.6 | 1.2 | 0.3 | 2.3 | 28.1 |
| Jrue Holiday | 98% | 30.7 | 15.4 | 5.0 | 5.3 | 2.4 | 1.2 | 0.3 | 2.4 | 25.7 |
| Ja Morant | 98% | 30.2 | 19.3 | 3.8 | 7.3 | 1.4 | 1.3 | 0.3 | 2.9 | 30.4 |
| Toumani Camara | 98% | 29.8 | 12.0 | 4.7 | 1.9 | 2.0 | 1.2 | 0.5 | 1.3 | 18.6 |
| Donovan Clingan | 98% | 26.2 | 11.2 | 11.5 | 2.0 | 1.1 | 0.7 | 2.1 | 1.3 | 24.8 |
| Sidy Cissoko | 93% | 22.7 | 6.3 | 3.3 | 1.8 | 0.7 | 1.1 | 0.4 | 1.1 | 11.4 |
| Scoot Henderson | 98% | 22.3 | 10.9 | 2.3 | 2.8 | 1.4 | 1.0 | 0.2 | 2.0 | 15.9 |
| Micah Potter | 52% | 14.5 | 6.2 | 4.2 | 0.9 | 0.7 | 0.4 | 0.3 | 0.9 | 11.2 |
| Vit Krejci | 96% | 11.9 | 4.2 | 1.7 | 1.0 | 0.6 | 0.5 | 0.2 | 0.4 | 6.8 |
| John Tonje | 16% | 8.7 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.5 | 5.9 |
| Branden Carlson | 16% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.5 | 5.9 |
| Yang Hansen | 52% | 8.0 | 2.7 | 2.0 | 0.5 | 0.1 | 0.2 | 0.3 | 0.8 | 5.2 |

</details>

<details><summary>if Ty Jerome plays: both teams</summary>

| Player | Plays | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 93% | 31.5 | 14.2 | 8.7 | 3.9 | 1.4 | 1.1 | 0.7 | 2.2 | 26.9 |
| Ty Jerome (MEM) | 100% | 28.9 | 21.9 | 3.3 | 6.3 | 2.2 | 1.2 | 0.3 | 2.5 | 31.4 |
| Cedric Coward (MEM) | 98% | 27.3 | 11.2 | 6.4 | 2.8 | 1.3 | 0.9 | 0.6 | 1.9 | 20.4 |
| Jaylen Wells (MEM) | 98% | 27.0 | 10.9 | 3.3 | 1.6 | 1.4 | 1.1 | 0.2 | 1.1 | 15.8 |
| Jerami Grant (MEM) | 98% | 23.3 | 10.2 | 2.6 | 1.8 | 1.2 | 0.8 | 0.7 | 1.5 | 14.6 |
| Zach Edey (MEM) | 98% | 21.4 | 8.2 | 8.1 | 1.2 | 0.1 | 0.6 | 1.5 | 1.5 | 17.6 |
| Cam Spencer (MEM) | 96% | 17.9 | 6.8 | 2.1 | 4.0 | 0.9 | 0.7 | 0.1 | 0.9 | 12.9 |
| Scotty Pippen Jr. (MEM) | 97% | 16.1 | 7.4 | 2.4 | 3.0 | 0.6 | 1.1 | 0.3 | 1.5 | 12.9 |
| GG Jackson (MEM) | 96% | 15.4 | 7.7 | 3.1 | 1.1 | 0.7 | 0.5 | 0.6 | 1.2 | 11.9 |
| Isaiah Stewart (MEM) | 98% | 14.3 | 5.5 | 3.2 | 0.7 | 0.3 | 0.3 | 0.9 | 0.7 | 9.4 |
| Quinten Post (MEM) | 88% | 12.6 | 4.2 | 2.4 | 0.6 | 0.4 | 0.3 | 0.4 | 0.6 | 7.2 |
| Olivier-Maxence Prosper (MEM) | 30% | 12.4 | 6.2 | 2.5 | 0.7 | 0.5 | 0.6 | 0.2 | 0.7 | 9.4 |
| Karim Lopez (MEM) | 23% | 12.3 | 5.3 | 2.3 | 1.1 | 0.4 | 0.4 | 0.2 | 0.6 | 8.7 |
| Kris Murray (MEM) | 48% | 9.5 | 2.3 | 1.6 | 0.8 | 0.1 | 0.4 | 0.2 | 0.4 | 4.6 |
| Taylor Hendricks (MEM) | 52% | 8.2 | 2.9 | 1.6 | 0.4 | 0.2 | 0.5 | 0.3 | 0.4 | 4.9 |
| Deni Avdija (POR) | 97% | 34.3 | 23.9 | 7.9 | 6.3 | 1.9 | 0.9 | 0.7 | 3.8 | 38.2 |
| Damian Lillard (POR) | 98% | 31.9 | 18.5 | 4.4 | 5.0 | 2.6 | 1.2 | 0.3 | 2.3 | 27.9 |
| Jrue Holiday (POR) | 98% | 30.6 | 15.5 | 4.9 | 5.3 | 2.4 | 1.1 | 0.3 | 2.4 | 25.7 |
| Ja Morant (POR) | 98% | 30.2 | 19.2 | 3.8 | 7.3 | 1.4 | 1.3 | 0.3 | 2.9 | 30.2 |
| Toumani Camara (POR) | 98% | 29.9 | 12.0 | 4.8 | 1.9 | 2.0 | 1.2 | 0.5 | 1.3 | 18.7 |
| Donovan Clingan (POR) | 98% | 26.2 | 11.2 | 11.5 | 2.0 | 1.1 | 0.7 | 2.1 | 1.3 | 24.7 |
| Sidy Cissoko (POR) | 93% | 22.6 | 6.2 | 3.2 | 1.8 | 0.7 | 1.1 | 0.4 | 1.1 | 11.3 |
| Scoot Henderson (POR) | 98% | 22.4 | 10.9 | 2.3 | 2.8 | 1.4 | 1.0 | 0.2 | 2.0 | 16.1 |
| Micah Potter (POR) | 52% | 14.4 | 6.1 | 4.1 | 0.9 | 0.6 | 0.4 | 0.3 | 0.9 | 11.1 |
| Vit Krejci (POR) | 96% | 11.9 | 4.1 | 1.7 | 1.0 | 0.6 | 0.5 | 0.2 | 0.4 | 6.8 |
| Branden Carlson (POR) | 16% | 8.7 | 3.6 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 |
| John Tonje (POR) | 16% | 8.7 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 |
| Yang Hansen (POR) | 52% | 8.1 | 2.7 | 2.1 | 0.5 | 0.1 | 0.2 | 0.3 | 0.8 | 5.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-29/`._
