"""Build leak-free feature frames P (player-game) and G (game) from processed history."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nbamodel.dataset import DATA, build, load_history  # noqa: E402

if __name__ == "__main__":
    pg, g = load_history()
    P, G = build(pg, g)
    P.to_parquet(DATA / "P.parquet", index=False)
    G.to_parquet(DATA / "G.parquet", index=False)
    print(P.shape, G.shape)
