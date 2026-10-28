# vs_opponent: before vs after

Train through 2023-24, test on 2025-26. Mean absolute error, lower is better.

| group                                | model   |   rows |   min MAE |   pts MAE |   reb MAE |   ast MAE |   fg3m MAE |
|:-------------------------------------|:--------|-------:|----------:|----------:|----------:|----------:|-----------:|
| all players                          | before  |  28328 |     4.36  |     4.346 |     1.81  |     1.299 |      0.868 |
| all players                          | after   |  28328 |     4.36  |     4.347 |     1.81  |     1.3   |      0.867 |
| traded (<15 games with new team)     | before  |   2778 |     4.629 |     3.913 |     1.639 |     1.159 |      0.771 |
| traded (<15 games with new team)     | after   |   2778 |     4.629 |     3.912 |     1.64  |     1.161 |      0.772 |
| back from long absence (<10 games)   | before  |   2859 |     4.454 |     3.81  |     1.614 |     1.154 |      0.717 |
| back from long absence (<10 games)   | after   |   2859 |     4.454 |     3.81  |     1.618 |     1.154 |      0.714 |
| first 10 games of the season         | before  |   5250 |     4.574 |     4.042 |     1.718 |     1.213 |      0.798 |
| first 10 games of the season         | after   |   5250 |     4.574 |     4.038 |     1.718 |     1.215 |      0.797 |
| same-position teammate out (20+ min) | before  |  12190 |     4.627 |     4.506 |     1.77  |     1.393 |      0.933 |
| same-position teammate out (20+ min) | after   |  12190 |     4.627 |     4.505 |     1.769 |     1.396 |      0.933 |
| playmakers (5+ ast per 36)           | before  |   5287 |     3.998 |     4.832 |     1.706 |     1.988 |      0.999 |
| playmakers (5+ ast per 36)           | after   |   5287 |     3.998 |     4.828 |     1.709 |     1.991 |      0.998 |
| 60+ past minutes vs this opponent    | before  |  20145 |     4.139 |     4.601 |     1.876 |     1.374 |      0.928 |
| 60+ past minutes vs this opponent    | after   |  20145 |     4.139 |     4.601 |     1.876 |     1.374 |      0.927 |
