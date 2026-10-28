# shot_quality: before vs after

Train through 2024-25, test on 2025-26. Mean absolute error, lower is better.

| group                                | model   |   rows |   min MAE |   pts MAE |   reb MAE |   ast MAE |   fg3m MAE |
|:-------------------------------------|:--------|-------:|----------:|----------:|----------:|----------:|-----------:|
| all players                          | before  |  28328 |     4.352 |     4.347 |     1.81  |     1.296 |      0.868 |
| all players                          | after   |  28328 |     4.352 |     4.348 |     1.811 |     1.296 |      0.869 |
| traded (<15 games with new team)     | before  |   2778 |     4.637 |     3.922 |     1.646 |     1.159 |      0.773 |
| traded (<15 games with new team)     | after   |   2778 |     4.637 |     3.923 |     1.644 |     1.162 |      0.774 |
| back from long absence (<10 games)   | before  |   2859 |     4.418 |     3.817 |     1.621 |     1.15  |      0.715 |
| back from long absence (<10 games)   | after   |   2859 |     4.418 |     3.818 |     1.62  |     1.149 |      0.717 |
| first 10 games of the season         | before  |   5250 |     4.559 |     4.044 |     1.723 |     1.212 |      0.8   |
| first 10 games of the season         | after   |   5250 |     4.559 |     4.052 |     1.722 |     1.213 |      0.8   |
| same-position teammate out (20+ min) | before  |  12190 |     4.62  |     4.505 |     1.77  |     1.39  |      0.933 |
| same-position teammate out (20+ min) | after   |  12190 |     4.62  |     4.509 |     1.77  |     1.391 |      0.934 |
| playmakers (5+ ast per 36)           | before  |   5287 |     3.992 |     4.838 |     1.708 |     1.981 |      0.998 |
| playmakers (5+ ast per 36)           | after   |   5287 |     3.992 |     4.839 |     1.706 |     1.98  |      0.999 |
