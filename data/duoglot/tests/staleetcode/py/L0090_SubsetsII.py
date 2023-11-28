
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2]]
    # output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
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
### subsetsWithDup 
from typing import *
def f_gold(nums: List[int]) -> List[List[int]]:
    def dfs(u, t):
        ans.append(t[:])
        for i in range(u, len(nums)):
            if i != u and nums[i] == nums[i - 1]:
                continue
            t.append(nums[i])
            dfs(i + 1, t)
            t.pop()
    ans = []
    nums.sort()
    dfs(0, [])
    return ans
"-----------------"
test()

