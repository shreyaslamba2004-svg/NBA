# ot_adjust: before vs after

Train through 2023-24, test on 2025-26. Mean absolute error, lower is better.

| group                                | model   |   rows |   min MAE |   pts MAE |   reb MAE |   ast MAE |   fg3m MAE |
|:-------------------------------------|:--------|-------:|----------:|----------:|----------:|----------:|-----------:|
| all players                          | before  |  28328 |     4.361 |     4.349 |     1.81  |     1.298 |      0.868 |
| all players                          | after   |  28328 |     4.36  |     4.348 |     1.81  |     1.298 |      0.868 |
| traded (<15 games with new team)     | before  |   2778 |     4.641 |     3.916 |     1.642 |     1.157 |      0.774 |
| traded (<15 games with new team)     | after   |   2778 |     4.629 |     3.911 |     1.639 |     1.157 |      0.773 |
| back from long absence (<10 games)   | before  |   2859 |     4.458 |     3.811 |     1.615 |     1.153 |      0.717 |
| back from long absence (<10 games)   | after   |   2859 |     4.454 |     3.805 |     1.614 |     1.153 |      0.716 |
| first 10 games of the season         | before  |   5250 |     4.581 |     4.05  |     1.718 |     1.212 |      0.8   |
| first 10 games of the season         | after   |   5250 |     4.574 |     4.047 |     1.718 |     1.213 |      0.799 |
| same-position teammate out (20+ min) | before  |  12190 |     4.631 |     4.508 |     1.769 |     1.393 |      0.933 |
| same-position teammate out (20+ min) | after   |  12190 |     4.627 |     4.508 |     1.77  |     1.393 |      0.933 |
| playmakers (5+ ast per 36)           | before  |   5287 |     4.008 |     4.837 |     1.707 |     1.988 |      0.997 |
| playmakers (5+ ast per 36)           | after   |   5287 |     3.998 |     4.832 |     1.706 |     1.987 |      0.997 |
| 60+ past minutes vs this opponent    | before  |  20145 |     4.141 |     4.605 |     1.875 |     1.372 |      0.928 |
| 60+ past minutes vs this opponent    | after   |  20145 |     4.139 |     4.603 |     1.876 |     1.372 |      0.928 |
