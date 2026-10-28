# pos_absence: before vs after

Train through 2023-24, test on 2025-26. Mean absolute error, lower is better.

| group                                | model   |   rows |   min MAE |   pts MAE |   reb MAE |   ast MAE |   fg3m MAE |
|:-------------------------------------|:--------|-------:|----------:|----------:|----------:|----------:|-----------:|
| all players                          | before  |  28328 |     4.37  |     4.351 |     1.811 |     1.298 |      0.869 |
| all players                          | after   |  28328 |     4.361 |     4.349 |     1.81  |     1.298 |      0.868 |
| traded (<15 games with new team)     | before  |   2778 |     4.644 |     3.916 |     1.651 |     1.155 |      0.774 |
| traded (<15 games with new team)     | after   |   2778 |     4.641 |     3.916 |     1.642 |     1.157 |      0.774 |
| back from long absence (<10 games)   | before  |   2859 |     4.464 |     3.827 |     1.621 |     1.154 |      0.717 |
| back from long absence (<10 games)   | after   |   2859 |     4.458 |     3.811 |     1.615 |     1.153 |      0.717 |
| first 10 games of the season         | before  |   5250 |     4.59  |     4.054 |     1.721 |     1.212 |      0.799 |
| first 10 games of the season         | after   |   5250 |     4.581 |     4.05  |     1.718 |     1.212 |      0.8   |
| same-position teammate out (20+ min) | before  |  12190 |     4.634 |     4.499 |     1.765 |     1.388 |      0.93  |
| same-position teammate out (20+ min) | after   |  12190 |     4.631 |     4.508 |     1.769 |     1.393 |      0.933 |
