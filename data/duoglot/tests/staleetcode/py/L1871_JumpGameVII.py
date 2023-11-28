
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["011010", 2, 3]
    # output: true
    # EXPLANATION:  In the first step, move from index 0 to index 3.  In the second step, move from index 3 to index 5.
    ,
    # example 2
    ["01101110", 2, 3]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canReach 
from typing import *
def f_gold(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    dp = [False] * n
    dp[0] = True
    pre_sum = [0] * (n + 1)
    pre_sum[1] = 1
    for i in range(1, n):
        if s[i] == '0':
            l = max(0, i - maxJump)
            r = i - minJump
            if r >= l and pre_sum[r + 1] - pre_sum[l] > 0:
                dp[i] = True
        pre_sum[i + 1] = pre_sum[i] + dp[i]
    return dp[n - 1]
"-----------------"
test()

