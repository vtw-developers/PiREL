
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 10, 5], [3, 0, 5, 3], 5]
    # output: [5,10]
    # EXPLANATION:  The processes colored in red are the processes that should be killed.
    ,
    # example 2
    [[1], [0], 1]
    # output: [1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### killProcess 
from collections import defaultdict
from typing import *
def f_gold(pid: List[int], ppid: List[int], kill: int) -> List[int]:
    def dfs(u):
        ans.append(u)
        for v in g[u]:
            dfs(v)
    g = defaultdict(list)
    n = len(pid)
    for c, p in zip(pid, ppid):
        g[p].append(c)
    ans = []
    dfs(kill)
    return ans
"-----------------"
test()

