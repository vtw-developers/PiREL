
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [0, 2]]]
    # output: 2
    # EXPLANATION:  The longest path of the tree is the path 1 - 0 - 2.
    ,
    # example 2
    [[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]]
    # output: 4
    # EXPLANATION:  The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### treeDiameter 
from collections import defaultdict
from typing import *
def f_gold(edges: List[List[int]]) -> int:
    def dfs(u, t):
        nonlocal ans, vis, d, next
        if vis[u]:
            return
        vis[u] = True
        for v in d[u]:
            dfs(v, t + 1)
        if ans < t:
            ans = t
            next = u
    d = defaultdict(set)
    vis = [False] * (len(edges) + 1)
    for u, v in edges:
        d[u].add(v)
        d[v].add(u)
    ans = 0
    next = 0
    dfs(edges[0][0], 0)
    vis = [False] * (len(edges) + 1)
    dfs(next, 0)
    return ans
"-----------------"
test()

