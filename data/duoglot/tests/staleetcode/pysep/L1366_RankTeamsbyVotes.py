### rankTeams 
from collections import defaultdict
from typing import *
def f_gold(votes: List[str]) -> str:
    d = defaultdict(lambda: [0] * len(votes[0]))
    for vote in votes:
        for i, v in enumerate(vote):
            d[v][i] -= 1
    ans = sorted(votes[0], key=lambda x: (d[x], x))
    return ''.join(ans)