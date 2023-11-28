
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], 1]
    # output: 4
    # EXPLANATION: The longest arithmetic subsequence is [1,2,3,4].
    ,
    # example 2
    [[1, 3, 5, 7], 1]
    # output: 1
    # EXPLANATION: The longest arithmetic subsequence is any single element.
    ,
    # example 3
    [[1, 5, 7, 8, 5, 3, 4, 2, 1], -2]
    # output: 4
    # EXPLANATION: The longest arithmetic subsequence is [7,5,3,1].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestSubsequence 
from collections import defaultdict
from typing import *
def f_gold(arr: List[int], difference: int) -> int:
    dp, ans = defaultdict(int), 1
    for num in arr:
        dp[num] = dp[num - difference] + 1
        ans = max(ans, dp[num])
    return ans
"-----------------"
test()

