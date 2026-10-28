"""Team name/abbreviation normalisation across sources (nba.com, ESPN, odds feeds)."""
from __future__ import annotations

TEAMS = {  # tricode: (team_id, full name, aliases)
    "ATL": (1610612737, "Atlanta Hawks", []),
    "BOS": (1610612738, "Boston Celtics", []),
    "BKN": (1610612751, "Brooklyn Nets", ["NJN", "New Jersey Nets", "BK", "BRK"]),
    "CHA": (1610612766, "Charlotte Hornets", ["Charlotte Bobcats", "CHO"]),
    "CHI": (1610612741, "Chicago Bulls", []),
    "CLE": (1610612739, "Cleveland Cavaliers", []),
    "DAL": (1610612742, "Dallas Mavericks", []),
    "DEN": (1610612743, "Denver Nuggets", []),
    "DET": (1610612765, "Detroit Pistons", []),
    "GSW": (1610612744, "Golden State Warriors", ["GS"]),
    "HOU": (1610612745, "Houston Rockets", []),
    "IND": (1610612754, "Indiana Pacers", []),
    "LAC": (1610612746, "LA Clippers", ["Los Angeles Clippers"]),
    "LAL": (1610612747, "Los Angeles Lakers", ["LA Lakers"]),
    "MEM": (1610612763, "Memphis Grizzlies", []),
    "MIA": (1610612748, "Miami Heat", []),
    "MIL": (1610612749, "Milwaukee Bucks", []),
    "MIN": (1610612750, "Minnesota Timberwolves", []),
    "NOP": (1610612740, "New Orleans Pelicans", ["NOH", "New Orleans Hornets", "NO"]),
    "NYK": (1610612752, "New York Knicks", ["NY"]),
    "OKC": (1610612760, "Oklahoma City Thunder", []),
    "ORL": (1610612753, "Orlando Magic", []),
    "PHI": (1610612755, "Philadelphia 76ers", []),
    "PHX": (1610612756, "Phoenix Suns", ["PHO"]),
    "POR": (1610612757, "Portland Trail Blazers", []),
    "SAC": (1610612758, "Sacramento Kings", []),
    "SAS": (1610612759, "San Antonio Spurs", ["SA"]),
    "TOR": (1610612761, "Toronto Raptors", []),
    "UTA": (1610612762, "Utah Jazz", ["UTAH"]),
    "WAS": (1610612764, "Washington Wizards", ["WSH"]),
}
_LOOKUP: dict[str, str] = {}
for tri, (tid, name, aliases) in TEAMS.items():
    for k in [tri, name, str(tid), name.split()[-1], *aliases]:
        _LOOKUP[k.upper()] = tri
_LOOKUP["TRAIL BLAZERS"] = "POR"
_LOOKUP["BLAZERS"] = "POR"


def canonical_team(x) -> str | None:
    if x is None or (isinstance(x, float) and x != x):
        return None
    return _LOOKUP.get(str(x).strip().upper(), str(x).strip().upper())


def team_id(tri: str) -> int:
    return TEAMS[canonical_team(tri)][0]
