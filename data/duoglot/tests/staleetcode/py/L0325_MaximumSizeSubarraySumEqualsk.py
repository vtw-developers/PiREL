
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, -1, 5, -2, 3], 3]
    # output: 4
    # EXPLANATION:  The subarray [1, -1, 5, -2] sums to 3 and is the longest.
    ,
    # example 2
    [[-2, -1, 2, 1], 1]
    # output: 2
    # EXPLANATION:  The subarray [-1, 2] sums to 1 and is the longest.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxSubArrayLen 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    mp = {0: -1}
    s = ans = 0
    for i, v in enumerate(nums):
        s += v
        if s - k in mp:
            ans = max(ans, i - mp[s - k])
        if s not in mp:
            mp[s] = i
    return ans
"-----------------"
test()

