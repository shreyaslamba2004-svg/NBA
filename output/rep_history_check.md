# rep_history: before vs after

Train through 2023-24, test on 2025-26. Mean absolute error, lower is better.

| group                                | model   |   rows |   min MAE |   pts MAE |   reb MAE |   ast MAE |   fg3m MAE |
|:-------------------------------------|:--------|-------:|----------:|----------:|----------:|----------:|-----------:|
| all players                          | before  |  28328 |     4.346 |     4.347 |     1.808 |     1.298 |      0.868 |
| all players                          | after   |  28328 |     4.337 |     4.339 |     1.809 |     1.297 |      0.868 |
| traded (<15 games with new team)     | before  |   2778 |     4.683 |     3.964 |     1.648 |     1.165 |      0.775 |
| traded (<15 games with new team)     | after   |   2778 |     4.621 |     3.919 |     1.64  |     1.158 |      0.771 |
| back from long absence (<10 games)   | before  |   2859 |     4.404 |     3.812 |     1.621 |     1.153 |      0.716 |
| back from long absence (<10 games)   | after   |   2859 |     4.383 |     3.792 |     1.613 |     1.15  |      0.715 |
| first 10 games of the season         | before  |   5250 |     4.577 |     4.057 |     1.72  |     1.216 |      0.799 |
| first 10 games of the season         | after   |   5250 |     4.564 |     4.036 |     1.722 |     1.211 |      0.797 |
| same-position teammate out (20+ min) | before  |  12190 |     4.613 |     4.515 |     1.768 |     1.394 |      0.933 |
| same-position teammate out (20+ min) | after   |  12190 |     4.603 |     4.506 |     1.769 |     1.392 |      0.933 |
| playmakers (5+ ast per 36)           | before  |   5287 |     3.965 |     4.832 |     1.706 |     1.982 |      0.998 |
| playmakers (5+ ast per 36)           | after   |   5287 |     3.965 |     4.831 |     1.708 |     1.982 |      0.998 |
