
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4]
    # output: 0.16666666666666666
    # EXPLANATION:  The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after <strong>second 1</strong> and then jumping with 1/2 probability to vertex 4 after <strong>second 2</strong>. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666.
    ,
    # example 2
    [7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7]
    # output: 0.3333333333333333
    # EXPLANATION: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after <strong>second 1</strong>.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### frogPosition 
from collections import deque
from collections import defaultdict
from typing import *
def f_gold(n: int, edges: List[List[int]], t: int, target: int
) -> float:
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    q = deque([(1, 1.0)])
    vis = [False] * (n + 1)
    vis[1] = True
    while q and t >= 0:
        for _ in range(len(q)):
            u, p = q.popleft()
            nxt = [v for v in g[u] if not vis[v]]
            if u == target and (not nxt or t == 0):
                return p
            for v in nxt:
                vis[v] = True
                q.append((v, p / len(nxt)))
        t -= 1
    return 0
"-----------------"
test()

