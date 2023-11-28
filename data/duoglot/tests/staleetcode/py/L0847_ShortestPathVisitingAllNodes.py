
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [0], [0], [0]]]
    # output: 4
    # EXPLANATION:  One possible path is [1,0,2,0,3]
    ,
    # example 2
    [[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]]
    # output: 4
    # EXPLANATION:  One possible path is [0,1,4,2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestPathLength 
from collections import deque
from typing import *
def f_gold(graph: List[List[int]]) -> int:
    n = len(graph)
    dst = -1 ^ (-1 << n)
    q = deque()
    vis = [[False] * (1 << n) for _ in range(n)]
    for i in range(n):
        q.append((i, 1 << i, 0))
        vis[i][1 << i] = True
    while q:
        u, state, dis = q.popleft()
        for v in graph[u]:
            nxt = state | (1 << v)
            if nxt == dst:
                return dis + 1
            if not vis[v][nxt]:
                q.append((v, nxt, dis + 1))
                vis[v][nxt] = True
    return 0
"-----------------"
test()

