
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -1]]
    # output: 2
    ,
    # example 2
    [7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -2]]
    # output: 6
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### deleteTreeNodes 
from collections import defaultdict
from typing import *
def f_gold(nodes: int, parent: List[int], value: List[int]) -> int:
    def dfs(u):
        for v in g[u]:
            dfs(v)
            value[u] += value[v]
            counter[u] += counter[v]
        if value[u] == 0:
            counter[u] = 0
    g = defaultdict(list)
    for i, p in enumerate(parent):
        if p != -1:
            g[p].append(i)
    counter = [1] * nodes
    dfs(0)
    return counter[0]
"-----------------"
test()

