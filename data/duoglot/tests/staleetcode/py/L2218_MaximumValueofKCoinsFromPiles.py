
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 100, 3], [7, 8, 9]], 2]
    # output: 101
    # EXPLANATION:  The above diagram shows the different ways we can choose k coins. The maximum total we can obtain is 101.
    ,
    # example 2
    [[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7]
    # output: 706
    # EXPLANATION: The maximum total can be obtained if we choose all coins from the last pile.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxValueOfCoins 
from itertools import accumulate
from typing import *
def f_gold(piles: List[List[int]], k: int) -> int:
    presum = [list(accumulate(p, initial=0)) for p in piles]
    dp = [0] * (k + 1)
    for s in presum:
        for j in range(k, -1, -1):
            for idx, v in enumerate(s):
                if j >= idx:
                    dp[j] = max(dp[j], dp[j - idx] + v)
    return dp[-1]
"-----------------"
test()

