
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 1], [0, 2], [0, 3], [1, 4]]]
    # output: true
    ,
    # example 2
    [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### validTree 
from typing import *
def f_gold(n: int, edges: List[List[int]]) -> bool:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    p = list(range(n))
    for a, b in edges:
        if find(a) == find(b):
            return False
        p[find(a)] = find(b)
        n -= 1
    return n == 1
"-----------------"
test()

