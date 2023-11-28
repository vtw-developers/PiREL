
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, 2]
    # output: [  [2,4],  [3,4],  [2,3],  [1,2],  [1,3],  [1,4],]
    ,
    # example 2
    [1, 1]
    # output: [[1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### combine 
from typing import *
def f_gold(n: int, k: int) -> List[List[int]]:
    res = []
    def dfs(i, n, k, t):
        if len(t) == k:
            res.append(t.copy())
            return
        for j in range(i, n + 1):
            t.append(j)
            dfs(j + 1, n, k, t)
            t.pop()
    dfs(1, n, k, [])
    return res
"-----------------"
test()

