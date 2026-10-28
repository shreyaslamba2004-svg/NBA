# rep_history: before vs after

Train through 2023-24, test on 2025-26. Mean absolute error, lower is better.

| group                                | model   |   rows |   min MAE |   pts MAE |   reb MAE |   ast MAE |   fg3m MAE |
|:-------------------------------------|:--------|-------:|----------:|----------:|----------:|----------:|-----------:|
| all players                          | before  |  28328 |     4.371 |     4.355 |     1.812 |     1.299 |      0.868 |
| all players                          | after   |  28328 |     4.37  |     4.351 |     1.811 |     1.298 |      0.869 |
| traded (<15 games with new team)     | before  |   2778 |     4.68  |     3.953 |     1.652 |     1.166 |      0.773 |
| traded (<15 games with new team)     | after   |   2778 |     4.644 |     3.916 |     1.651 |     1.155 |      0.774 |
| back from long absence (<10 games)   | before  |   2859 |     4.442 |     3.822 |     1.618 |     1.148 |      0.715 |
| back from long absence (<10 games)   | after   |   2859 |     4.464 |     3.827 |     1.621 |     1.154 |      0.717 |
| first 10 games of the season         | before  |   5250 |     4.6   |     4.071 |     1.722 |     1.217 |      0.799 |
| first 10 games of the season         | after   |   5250 |     4.59  |     4.054 |     1.721 |     1.212 |      0.799 |
| same-position teammate out (20+ min) | before  |  12190 |     4.629 |     4.502 |     1.767 |     1.39  |      0.931 |
| same-position teammate out (20+ min) | after   |  12190 |     4.634 |     4.499 |     1.765 |     1.388 |      0.93  |
