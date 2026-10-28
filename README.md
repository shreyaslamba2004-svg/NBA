# NBA projection model

**Today's sheet: [TODAY.md](TODAY.md)** (best bets, same-game multis, check-news flags and every
projection; Sydney time, decimal odds; rewritten on every scheduled run).

Projects every NBA game on a slate: final score, win probability, spread, total, and player
minutes / points / rebounds / assists / threes / steals / blocks / turnovers (+ PRA, PR, PA,
RA, stocks). It prices everything as fair odds and compares against market lines. It
re-projects when injury, rest or lineup news changes availability.

The projections come from statistical and machine-learning code (LightGBM + Monte Carlo
simulation), not from an LLM guessing.

## How it works

```
history (2010-11 .. today)              today's slate
  box scores, results, closing lines      ESPN schedule + rosters
        |                                 official NBA injury report PDF + ESPN injuries
        v                                         |
  leak-free features  <---------------------------+
   - player form: EWMA minutes, per-minute rates (short/long), usage, starter rate
   - availability: minutes/usage/value vacated by absent teammates, games missed
   - team: off/def rating, pace, 3pt rate (EWMA), rest, back-to-backs, games in 4/7 days
   - opponent: stat-specific per-possession allowances (reb, ast, 3pm, stl, blk, tov, pts)
        |
        v
  models (LightGBM)
   - minutes model -> normalised so each team plays 240 (+OT) minutes
   - per-minute rate model for each stat (minutes-weighted)
   - team margin + total models
        |
        v
  simulation (20k runs per game)
   - correlated team scores, overtime resolution
   - questionable players play with their status probability
   - player minutes noise, gamma-Poisson stat counts scaled by simulated game script
        |
        v
  outputs: projections, distributions, fair lines/odds, EV + Kelly vs market prices
```

## Data sources

| data | source | cost |
|---|---|---|
| Player box scores 2010-11 to 2023-24 | [NocturneBear/NBA-Data-2010-2024](https://github.com/NocturneBear/NBA-Data-2010-2024) (nba.com box scores) | free |
| Box scores 2024-25, 2025-26 | rebuilt from cdn.nba.com play-by-play ([shufinskiy/nba_data](https://github.com/shufinskiy/nba_data)); minutes/points/rebounds/assists match official boxes 99.8-100% | free |
| Closing lines 2007-08 to 2025-26 | [kyleskom/NBA-Machine-Learning-Sports-Betting](https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting) OddsData.sqlite | free |
| Current season box scores, schedule, rosters, injuries, officials | ESPN public API | free |
| Game lines (spread/total/ML, open + current) | DraftKings via ESPN | free |
| Player props (full DraftKings menu, open + current) | DraftKings via ESPN core API | free |
| Official injury report | ak-static.cms.nba.com PDF (every 15 min on game days) | free |
| Other books' prop prices (optional) | [The Odds API](https://the-odds-api.com), `ODDS_API_KEY` | free tier 500 credits/month |

stats.nba.com and cdn.nba.com block most cloud/datacenter IPs. Everything here therefore
works from GitHub Actions and cloud machines without them. ESPN's endpoints are public but
undocumented: fine for personal use, and they may change without notice.

## Usage

```bash
pip install -r requirements.txt
python scripts/build_history.py        # download + unify history (~4 min)
python scripts/espn_dnp_backfill.py    # dressed-but-unused players for 2024-26 (see "Leakage")
python scripts/build_features.py       # feature frames (~3 min)
python scripts/train_backtest.py       # backtest report + models/bundle.pkl

python -m nbamodel.cli run                    # project today's slate -> output/<date>/
python -m nbamodel.cli watch --every 10       # re-project on any injury/rest change until tip
python -m nbamodel.cli snapshot --kind pretip # what the scheduled job runs (logs/)
```

Outputs in `output/<date>/`:
- `games.csv`: projected scores, margin, total, win %, fair moneyline/spread/total, cover and over probabilities at the market line
- `players.csv`: projected minutes and stats, fair line and over probability/odds for each stat and combo
- `edges.csv`: every market price with model probability, expected value and quarter-Kelly stake, sorted by EV
- `availability.csv`: who is expected to play, with status and play probability
- `sgm.csv`: suggested same-game multis priced from the joint simulation (`python -m nbamodel.cli sgm` checks a quoted one)
- `today.md`: the readable sheet, also copied to `TODAY.md` at the repo root

### How bets are chosen

- **Blend:** bet decisions use a blend of model and no-vig market probability. Weights are fitted, not
  guessed: `scripts/pit_backtest.py` fits them on 2024-25 and tests on 2025-26 with availability taken
  from the pre-game injury report. For sides, totals and moneylines the fitted model weight is **0**:
  the closing market already contains everything the model knows. Game-line "best bets" are therefore
  pure line shopping (a book's price beating the all-book no-vig consensus). Props use 0.25 until the
  logs hold enough graded props to fit it (`nbamodel/monitor.py` refits weekly). Results:
  `output/pit_backtest.md`.
- **Best bets:** blended EV of at least 5%, at odds of 4.0 or shorter, with a quarter-Kelly stake capped at
  2% of bankroll.
- **Check news first:** the model and the market disagree by more than 15 points. That usually means news
  the model hasn't seen, such as a player returning from injury with no NBA history.
- **Questionable players:** every game is projected with all questionable players sitting (the tables
  for confirmed players), plus "if he plays" versions in which teammates, the opponent and the game line
  all adjust. Bets are priced on the probability-weighted mix; bets that hinge on a questionable player
  go to "Wait for news". Once his status is confirmed, the next run collapses the game to one projection.
- **Same-game multis:** capped at a combined price of 2.5.
- **Chance to play:** healthy players are scaled by a calibrated chance the coach uses them
  (`nbamodel/rotation.py`). Without it the deep bench soaks up starters' minutes.

## Scheduled logging (GitHub Actions)

`.github/workflows/daily.yml` runs a morning snapshot at 15:00 UTC and then every 15 minutes
from 21:00 to 05:45 UTC (about 8am to 4:45pm Sydney). It re-projects when injury or lineup news
changes, and buys AU prop prices for each game about 40 minutes before tip. Each run:
1. grades yesterday: final scores and player lines go to `logs/results/`
2. pulls new box scores and refreshes the current season
3. projects today's slate
4. appends game lines and every prop price to `logs/market/`, and projections to `logs/projections/`

Over time this builds your own model-vs-market record. The `ODDS_API_KEY` repository secret
adds AU bookmaker prices (Sportsbet, PointsBet, Ladbrokes, Neds, Unibet and others).

## Leakage and honesty notes

- All features use only games before the one being predicted.
- Availability in training means "who was available": players who played plus players
  who dressed but got a coach's-decision DNP. An earlier version counted every
  non-participant as absent. That leaks game script, since deep benches only play in
  blowouts, and it produced an unrealistically strong backtest against closing lines.
- In backtests, availability is known from box scores. Live, it comes from injury reports,
  which miss some late scratches.
- See `output/backtest_report.md` for the current walk-forward results. On 2025-26 the pure model
  does not beat closing lines on sides (margin MAE 10.93 vs 10.60, ATS 47-50%). Player minutes and
  stat projections beat simple baselines. Treat edges as leads to check, not certainties.
