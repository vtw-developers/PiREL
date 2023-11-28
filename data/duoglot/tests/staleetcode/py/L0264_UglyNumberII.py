
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10]
    # output: 12
    # EXPLANATION:  [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
    ,
    # example 2
    [1]
    # output: 1
    # EXPLANATION:  1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### nthUglyNumber 
from typing import *
def f_gold(n: int) -> int:
    dp = [1] * n
    p2 = p3 = p5 = 0
    for i in range(1, n):
        next2, next3, next5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
        dp[i] = min(next2, next3, next5)
        if dp[i] == next2:
            p2 += 1
        if dp[i] == next3:
            p3 += 1
        if dp[i] == next5:
            p5 += 1
    return dp[n - 1]
"-----------------"
test()

