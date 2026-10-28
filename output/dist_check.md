# Stat distribution check (2025-26 held out)

Coverage: share of actual results inside the model's middle 50% / 80% range (ideal 0.50 / 0.80). Log loss is for over/under at lines around the median (lower is better).

| stat   | variant             |   over_under_logloss |   coverage_50 |   coverage_80 |
|:-------|:--------------------|---------------------:|--------------:|--------------:|
| ast    | count noise x0.7    |               0.4058 |        0.4869 |        0.7879 |
| ast    | count noise x1.5    |               0.4061 |        0.5031 |        0.7988 |
| ast    | count noise x2.5    |               0.4054 |        0.5031 |        0.8129 |
| ast    | current             |               0.4054 |        0.499  |        0.8036 |
| ast    | minutes noise x0.75 |               0.4075 |        0.4732 |        0.7882 |
| ast    | minutes noise x1.25 |               0.4058 |        0.5036 |        0.8087 |
| blk    | count noise x0.7    |               0.5247 |        0.5099 |        0.7968 |
| blk    | count noise x1.5    |               0.5252 |        0.5092 |        0.8014 |
| blk    | count noise x2.5    |               0.5266 |        0.499  |        0.8053 |
| blk    | current             |               0.5234 |        0.5072 |        0.8055 |
| blk    | minutes noise x0.75 |               0.5223 |        0.5001 |        0.7994 |
| blk    | minutes noise x1.25 |               0.5256 |        0.5096 |        0.8001 |
| fg3m   | count noise x0.7    |               0.5907 |        0.4483 |        0.7498 |
| fg3m   | count noise x1.5    |               0.6002 |        0.4548 |        0.7384 |
| fg3m   | count noise x2.5    |               0.6077 |        0.4453 |        0.7487 |
| fg3m   | current             |               0.5928 |        0.4544 |        0.7488 |
| fg3m   | minutes noise x0.75 |               0.5944 |        0.4583 |        0.7485 |
| fg3m   | minutes noise x1.25 |               0.5951 |        0.4624 |        0.7624 |
| pts    | count noise x0.7    |               0.6512 |        0.4349 |        0.7193 |
| pts    | count noise x1.5    |               0.6519 |        0.4737 |        0.7624 |
| pts    | count noise x2.5    |               0.6534 |        0.5163 |        0.8068 |
| pts    | current             |               0.6513 |        0.4544 |        0.7392 |
| pts    | minutes noise x0.75 |               0.6535 |        0.4321 |        0.7102 |
| pts    | minutes noise x1.25 |               0.6513 |        0.478  |        0.7754 |
| reb    | count noise x0.7    |               0.5133 |        0.4936 |        0.8005 |
| reb    | count noise x1.5    |               0.5138 |        0.5023 |        0.8083 |
| reb    | count noise x2.5    |               0.5146 |        0.5033 |        0.8101 |
| reb    | current             |               0.5141 |        0.499  |        0.7966 |
| reb    | minutes noise x0.75 |               0.515  |        0.4767 |        0.7808 |
| reb    | minutes noise x1.25 |               0.5148 |        0.5213 |        0.8192 |
| stl    | count noise x0.7    |               0.5859 |        0.4973 |        0.7962 |
| stl    | count noise x1.5    |               0.5911 |        0.498  |        0.8016 |
| stl    | count noise x2.5    |               0.5956 |        0.5068 |        0.8111 |
| stl    | current             |               0.5881 |        0.5098 |        0.8035 |
| stl    | minutes noise x0.75 |               0.5852 |        0.5042 |        0.8025 |
| stl    | minutes noise x1.25 |               0.5936 |        0.4988 |        0.8018 |

## Best variant per stat

| stat   | variant             |
|:-------|:--------------------|
| ast    | count noise x2.5    |
| blk    | minutes noise x0.75 |
| fg3m   | count noise x0.7    |
| pts    | count noise x0.7    |
| reb    | count noise x0.7    |
| stl    | minutes noise x0.75 |

## Where actual results landed in the current distributions (5 bins, ideal 0.20 each)

| stat   | share per bin (low to high)   |
|:-------|:------------------------------|
| ast    | 0.21 0.21 0.20 0.18 0.20      |
| blk    | 0.20 0.21 0.20 0.20 0.19      |
| fg3m   | 0.20 0.18 0.18 0.19 0.26      |
| pts    | 0.24 0.17 0.18 0.20 0.22      |
| reb    | 0.20 0.20 0.20 0.21 0.19      |
| stl    | 0.20 0.21 0.20 0.20 0.20      |
