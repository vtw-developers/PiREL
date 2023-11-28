
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 6, 7, 7]]
    # output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    ,
    # example 2
    [[4, 4, 3, 2, 1]]
    # output: [[4,4]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findSubsequences 
from typing import *
def f_gold(nums: List[int]) -> List[List[int]]:
    def dfs(u, last, t):
        if u == len(nums):
            if len(t) > 1:
                ans.append(t[:])
            return
        if nums[u] >= last:
            t.append(nums[u])
            dfs(u + 1, nums[u], t)
            t.pop()
        if nums[u] != last:
            dfs(u + 1, last, t)
    ans = []
    dfs(0, -1000, [])
    return ans
"-----------------"
test()

