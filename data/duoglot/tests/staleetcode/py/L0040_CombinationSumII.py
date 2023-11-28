
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 1, 2, 7, 6, 1, 5], 8]
    # output: [[1,1,6],[1,2,5],[1,7],[2,6]]
    ,
    # example 2
    [[2, 5, 2, 1, 2], 5]
    # output: [[1,2,2],[5]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### combinationSum2 
from typing import *
def f_gold(candidates: List[int], target: int) -> List[List[int]]:
    def dfs(u, s, t):
        if s > target:
            return
        if s == target:
            ans.append(t[:])
            return
        for i in range(u, len(candidates)):
            if i > u and candidates[i] == candidates[i - 1]:
                continue
            t.append(candidates[i])
            dfs(i + 1, s + candidates[i], t)
            t.pop()
    ans = []
    candidates.sort()
    dfs(0, 0, [])
    return ans
"-----------------"
test()

