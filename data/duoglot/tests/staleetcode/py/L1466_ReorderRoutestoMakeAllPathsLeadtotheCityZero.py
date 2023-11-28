
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]]
    # output: 3
    # EXPLANATION: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    ,
    # example 2
    [5, [[1, 0], [1, 2], [3, 2], [3, 4]]]
    # output: 2
    # EXPLANATION: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    ,
    # example 3
    [3, [[1, 0], [2, 0]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minReorder 
from collections import defaultdict
from typing import *
def f_gold(n: int, connections: List[List[int]]) -> int:
    def dfs(u):
        vis[u] = True
        ans = 0
        for v in g[u]:
            if not vis[v]:
                if (u, v) in s:
                    ans += 1
                ans += dfs(v)
        return ans
    g = defaultdict(list)
    s = set()
    for a, b in connections:
        g[a].append(b)
        g[b].append(a)
        s.add((a, b))
    vis = [False] * n
    return dfs(0)
"-----------------"
test()

