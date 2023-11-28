
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    ,
    # example 2
    [[0]]
    # output: [[],[0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### subsets 
from typing import *
def f_gold(nums: List[int]) -> List[List[int]]:
    def dfs(u, t):
        if u == len(nums):
            ans.append(t[:])
            return
        dfs(u + 1, t)
        t.append(nums[u])
        dfs(u + 1, t)
        t.pop()
    ans = []
    dfs(0, [])
    return ans
"-----------------"
test()

