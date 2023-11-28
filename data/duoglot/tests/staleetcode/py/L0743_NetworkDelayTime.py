
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2]
    # output: 2
    ,
    # example 2
    [[[1, 2, 1]], 2, 1]
    # output: 1
    ,
    # example 3
    [[[1, 2, 1]], 2, 2]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### networkDelayTime 
from heapq import heapify, heappush, heappop
from collections import defaultdict
from typing import *
def f_gold(times: List[List[int]], n: int, k: int) -> int:
    INF = 0x3F3F
    g = defaultdict(list)
    for u, v, w in times:
        g[u - 1].append((v - 1, w))
    dist = [INF] * n
    dist[k - 1] = 0
    q = [(0, k - 1)]
    while q:
        _, u = heappop(q)
        for v, w in g[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(q, (dist[v], v))
    ans = max(dist)
    return -1 if ans == INF else ans
"-----------------"
test()

