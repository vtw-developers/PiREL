
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]]
    # output: 6
    # EXPLANATION:  Choosing any 2 edges will connect all cities so we choose the minimum 2.
    ,
    # example 2
    [4, [[1, 2, 3], [3, 4, 4]]]
    # output: -1
    # EXPLANATION:  There is no way to connect all cities even if all edges are used.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumCost 
from typing import *
def f_gold(n: int, connections: List[List[int]]) -> int:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    connections.sort(key=lambda x: x[2])
    p = list(range(n))
    ans = 0
    for x, y, cost in connections:
        x, y = x - 1, y - 1
        if find(x) == find(y):
            continue
        p[find(x)] = find(y)
        ans += cost
        n -= 1
        if n == 1:
            return ans
    return -1
"-----------------"
test()

