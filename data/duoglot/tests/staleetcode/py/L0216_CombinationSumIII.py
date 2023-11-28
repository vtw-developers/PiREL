
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 7]
    # output: [[1,2,4]]
    # EXPLANATION:  1 + 2 + 4 = 7 There are no other valid combinations.
    ,
    # example 2
    [3, 9]
    # output: [[1,2,6],[1,3,5],[2,3,4]]
    # EXPLANATION:  1 + 2 + 6 = 9 1 + 3 + 5 = 9 2 + 3 + 4 = 9 There are no other valid combinations.
    ,
    # example 3
    [4, 1]
    # output: []
    # EXPLANATION:  There are no valid combinations. Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### combinationSum3 
from typing import *
def f_gold(k: int, n: int) -> List[List[int]]:
    def dfs(i, s, t):
        if i > 9 or s > n or len(t) > k:
            return
        if s == n and len(t) == k:
            ans.append(t[:])
            return
        i += 1
        t.append(i)
        dfs(i, s + i, t)
        t.pop()
        dfs(i, s, t)
    ans = []
    dfs(0, 0, [])
    return ans
"-----------------"
test()

