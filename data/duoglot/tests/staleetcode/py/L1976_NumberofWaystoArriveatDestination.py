
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]]
    # output: 4
    # EXPLANATION:  The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes. The four ways to get there in 7 minutes are: - 0   6 - 0   4   6 - 0   1   2   5   6 - 0   1   3   5   6
    ,
    # example 2
    [2, [[1, 0, 10]]]
    # output: 1
    # EXPLANATION:  There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countPaths 
import math
from math import inf
from typing import *
def f_gold(n: int, roads: List[List[int]]) -> int:
    INF = float('inf')
    MOD = 10**9 + 7
    g = [[INF] * n for _ in range(n)]
    for u, v, t in roads:
        g[u][v] = t
        g[v][u] = t
    g[0][0] = 0
    dist = [INF] * n
    w = [0] * n
    dist[0] = 0
    w[0] = 1
    vis = [False] * n
    for _ in range(n):
        t = -1
        for i in range(n):
            if not vis[i] and (t == -1 or dist[i] < dist[t]):
                t = i
        vis[t] = True
        for i in range(n):
            if i == t:
                continue
            ne = dist[t] + g[t][i]
            if dist[i] > ne:
                dist[i] = ne
                w[i] = w[t]
            elif dist[i] == ne:
                w[i] += w[t]
    return w[-1] % MOD
"-----------------"
test()

