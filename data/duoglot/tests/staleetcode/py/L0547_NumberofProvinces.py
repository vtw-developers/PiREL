
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 0], [1, 1, 0], [0, 0, 1]]]
    # output: 2
    ,
    # example 2
    [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findCircleNum 
from typing import *
def f_gold(isConnected: List[List[int]]) -> int:
    def dfs(i):
        vis[i] = True
        for j in range(n):
            if not vis[j] and isConnected[i][j]:
                dfs(j)
    n = len(isConnected)
    vis = [False] * n
    ans = 0
    for i in range(n):
        if not vis[i]:
            dfs(i)
            ans += 1
    return ans
"-----------------"
test()

