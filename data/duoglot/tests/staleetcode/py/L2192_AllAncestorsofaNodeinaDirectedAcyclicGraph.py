
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]]
    # output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    # EXPLANATION:  The above diagram represents the input graph. - Nodes 0, 1, and 2 do not have any ancestors. - Node 3 has two ancestors 0 and 1. - Node 4 has two ancestors 0 and 2. - Node 5 has three ancestors 0, 1, and 3. - Node 6 has five ancestors 0, 1, 2, 3, and 4. - Node 7 has four ancestors 0, 1, 2, and 3.
    ,
    # example 2
    [5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]]
    # output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
    # EXPLANATION:  The above diagram represents the input graph. - Node 0 does not have any ancestor. - Node 1 has one ancestor 0. - Node 2 has two ancestors 0 and 1. - Node 3 has three ancestors 0, 1, and 2. - Node 4 has four ancestors 0, 1, 2, and 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getAncestors 
from collections import deque
from collections import defaultdict
from typing import *
def f_gold(n: int, edges: List[List[int]]) -> List[List[int]]:
    g = defaultdict(list)
    for u, v in edges:
        g[v].append(u)
    ans = []
    for i in range(n):
        if not g[i]:
            ans.append([])
            continue
        q = deque([i])
        vis = [False] * n
        vis[i] = True
        t = []
        while q:
            for _ in range(len(q)):
                v = q.popleft()
                for u in g[v]:
                    if not vis[u]:
                        vis[u] = True
                        q.append(u)
                        t.append(u)
        ans.append(sorted(t))
    return ans
"-----------------"
test()

