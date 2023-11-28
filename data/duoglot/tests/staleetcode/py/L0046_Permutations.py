
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    ,
    # example 2
    [[0, 1]]
    # output: [[0,1],[1,0]]
    ,
    # example 3
    [[1]]
    # output: [[1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### permute 
from typing import *
def f_gold(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    path = [0] * n
    used = [False] * n
    def dfs(u):
        if u == n:
            res.append(path.copy())
            return
        for i in range(n):
            if not used[i]:
                path[u] = nums[i]
                used[i] = True
                dfs(u + 1)
                used[i] = False
    dfs(0)
    return res
"-----------------"
test()

