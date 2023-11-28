
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 1], [1, 2], [3, 4]]]
    # output: 2
    ,
    # example 2
    [5, [[0, 1], [1, 2], [2, 3], [3, 4]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countComponents 
from typing import *
def f_gold(n: int, edges: List[List[int]]) -> int:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    p = list(range(n))
    for a, b in edges:
        p[find(a)] = find(b)
    return sum(i == find(i) for i in range(n))
"-----------------"
test()

