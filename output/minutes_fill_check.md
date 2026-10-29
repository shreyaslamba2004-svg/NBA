# Minutes: fill to 240 or not? (live-like backtest)

2025-26 regular season, model trained through 2023-24. Candidates are everyone active for each game (players plus coach's-decision DNPs), as live where the rotation isn't known. Chance to play from the rotation model (fit on 2024-25), minutes-if-he-plays from the minutes model. Errors on players who played; buckets are by projected minutes/points, value = average projection minus actual.

```
expected team minutes before fill: mean 238.7, 10th pct 220.5, 90th pct 260.5
no fill              MAE 4.366 short 4.85 long 4.11 {'0-15': '+0.02', '15-25': '-0.13', '25-32': '+0.28', '32-36': '+0.30', '36-50': '+0.28'}
proportional (old)   MAE 4.602 short 5.42 long 4.64 {'0-15': '+0.24', '15-25': '-0.14', '25-32': '+0.26', '32-36': '+0.93', '36-50': '+3.76'}
headroom (today)     MAE 4.517 short 5.29 long 4.40 {'0-15': '+0.26', '15-25': '+0.00', '25-32': '+0.59', '32-36': '+0.88', '36-50': '+1.65'}
headroom half        MAE 4.396 short 4.93 long 4.17 {'0-15': '+0.24', '15-25': '-0.00', '25-32': '+0.39', '32-36': '+0.48', '36-50': '+0.49'}
headroom cap3        MAE 4.479 short 5.10 long 4.36 {'0-15': '+0.30', '15-25': '+0.00', '25-32': '+0.54', '32-36': '+0.70', '36-50': '+0.86'}
headroom half cap3   MAE 4.392 short 4.90 long 4.17 {'0-15': '+0.24', '15-25': '+0.00', '25-32': '+0.38', '32-36': '+0.44', '36-50': '+0.42'}
headroom cap2        MAE 4.455 short 5.02 long 4.30 {'0-15': '+0.33', '15-25': '-0.01', '25-32': '+0.47', '32-36': '+0.59', '36-50': '+0.86'}
--- points
no fill              reconcile       MAE 4.470 {'0-10': '+0.02', '10-18': '+0.06', '18-25': '+0.29', '25-60': '+1.82'}
no fill              half reconcile  MAE 4.447 {'0-10': '+0.06', '10-18': '-0.02', '18-25': '+0.10', '25-60': '+1.80'}
no fill              no reconcile    MAE 4.454 {'0-10': '+0.03', '10-18': '-0.06', '18-25': '+0.13', '25-60': '+2.24'}
proportional (old)   reconcile       MAE 4.470 {'0-10': '+0.02', '10-18': '+0.06', '18-25': '+0.29', '25-60': '+1.82'}
proportional (old)   half reconcile  MAE 4.481 {'0-10': '+0.06', '10-18': '+0.02', '18-25': '+0.29', '25-60': '+2.42'}
proportional (old)   no reconcile    MAE 4.506 {'0-10': '+0.07', '10-18': '+0.03', '18-25': '+0.42', '25-60': '+2.92'}
headroom (today)     reconcile       MAE 4.468 {'0-10': '+0.05', '10-18': '+0.09', '18-25': '+0.34', '25-60': '+1.44'}
headroom (today)     half reconcile  MAE 4.476 {'0-10': '+0.09', '10-18': '+0.08', '18-25': '+0.31', '25-60': '+2.04'}
headroom (today)     no reconcile    MAE 4.498 {'0-10': '+0.10', '10-18': '+0.10', '18-25': '+0.45', '25-60': '+2.29'}
headroom half cap3   reconcile       MAE 4.467 {'0-10': '+0.04', '10-18': '+0.08', '18-25': '+0.27', '25-60': '+1.63'}
headroom half cap3   half reconcile  MAE 4.457 {'0-10': '+0.08', '10-18': '+0.02', '18-25': '+0.21', '25-60': '+1.93'}
headroom half cap3   no reconcile    MAE 4.465 {'0-10': '+0.09', '10-18': '+0.00', '18-25': '+0.24', '25-60': '+2.27'}
```

Kept: no fill (minutes) and a half-strength pull of player points toward the team model's total.
