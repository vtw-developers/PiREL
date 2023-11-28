
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2]
    # output: 0.25000
    # EXPLANATION:  There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
    ,
    # example 2
    [3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2]
    # output: 0.30000
    ,
    # example 3
    [3, [[0, 1]], [0.5], 0, 2]
    # output: 0.00000
    # EXPLANATION:  There is no path between 0 and 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxProbability 
from heapq import heapify, heappush, heappop
from collections import defaultdict
from typing import *
def f_gold(n: int,
    edges: List[List[int]],
    succProb: List[float],
    start: int,
    end: int,
) -> float:
    g = defaultdict(list)
    for (a, b), s in zip(edges, succProb):
        g[a].append((b, s))
        g[b].append((a, s))
    q = [(-1, start)]
    d = [0] * n
    d[start] = 1
    while q:
        w, u = heappop(q)
        w = -w
        if d[u] > w:
            continue
        for v, t in g[u]:
            if d[v] < d[u] * t:
                d[v] = d[u] * t
                heappush(q, (-d[v], v))
    return d[end]
"-----------------"
test()

