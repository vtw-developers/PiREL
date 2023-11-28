
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[1, 2], [2, 3], [3, 1]]]
    # output: [1,2,3]
    # EXPLANATION:  Gardens 1 and 2 have different types. Gardens 2 and 3 have different types. Gardens 3 and 1 have different types. Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
    ,
    # example 2
    [4, [[1, 2], [3, 4]]]
    # output: [1,2,1,2]
    ,
    # example 3
    [4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]]
    # output: [1,2,3,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### gardenNoAdj 
from collections import defaultdict
from typing import *
def f_gold(n: int, paths: List[List[int]]) -> List[int]:
    g = defaultdict(list)
    for x, y in paths:
        x, y = x - 1, y - 1
        g[x].append(y)
        g[y].append(x)
    ans = [0] * n
    for u in range(n):
        colors = set(ans[v] for v in g[u])
        for c in range(1, 5):
            if c not in colors:
                ans[u] = c
                break
    return ans
"-----------------"
test()

