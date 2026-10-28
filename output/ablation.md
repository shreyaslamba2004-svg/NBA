# Context factors: keep or drop

Each row retrains without one factor (train through 2023-24, test on 2025-26). Lower is better. A factor is kept if removing it makes projections worse by more than 0.1% on average.

| variant                     |   min MAE |   pts MAE |   reb MAE |   ast MAE |   fg3m MAE |   margin MAE |   total MAE |   win logloss | verdict        |
|:----------------------------|----------:|----------:|----------:|----------:|-----------:|-------------:|------------:|--------------:|:---------------|
| all factors (current)       |    4.3602 |    4.3485 |    1.8097 |    1.2978 |     0.8683 |      11.2994 |     14.9923 |        0.5871 |                |
| without travel              |    4.3587 |    4.3473 |    1.8093 |    1.2972 |     0.8685 |      11.304  |     15.0559 |        0.5887 | keep (helps)   |
| without schedule_load       |    4.3623 |    4.3493 |    1.8097 |    1.2972 |     0.8683 |      11.2889 |     15.0195 |        0.5871 | drop (no help) |
| without rotation_depth      |    4.3594 |    4.3494 |    1.8096 |    1.2978 |     0.8684 |      11.3    |     15.0369 |        0.5868 | drop (no help) |
| without rest_habits         |    4.3604 |    4.3483 |    1.8093 |    1.2978 |     0.8682 |      11.3081 |     15.0292 |        0.5878 | keep (helps)   |
| without motivation          |    4.3669 |    4.3519 |    1.8097 |    1.3001 |     0.8683 |      11.3031 |     15.0583 |        0.5891 | keep (helps)   |
| without referees            |    4.3602 |    4.3483 |    1.8097 |    1.2978 |     0.8683 |      11.2832 |     15.0318 |        0.5863 | drop (no help) |
| without shooting_luck       |    4.3602 |    4.3427 |    1.8097 |    1.2978 |     0.8678 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
| without award_pressure      |    4.3594 |    4.3487 |    1.81   |    1.2977 |     0.8681 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
| without late_news           |    4.3512 |    4.3478 |    1.809  |    1.2972 |     0.8681 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
| without rep_history         |    4.3602 |    4.3524 |    1.8089 |    1.2984 |     0.8688 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
| without pos_absence         |    4.369  |    4.3513 |    1.8111 |    1.2975 |     0.8686 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
| without ot_adjust           |    4.3611 |    4.3494 |    1.8095 |    1.2977 |     0.8683 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
| defense vs player type only |    4.3602 |    4.3431 |    1.8106 |    1.3018 |     0.8698 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
| defense vs position only    |    4.3602 |    4.3536 |    1.8094 |    1.299  |     0.8699 |      11.2994 |     14.9923 |        0.5871 | drop (no help) |
