
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]]
    # output: 11
    # EXPLANATION:  The triangle looks like:    <u>2</u>   <u>3</u> 4  6 <u>5</u> 7 4 <u>1</u> 8 3 The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
    ,
    # example 2
    [[[-10]]]
    # output: -10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumTotal 
from typing import *
def f_gold(triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
    return dp[0]
"-----------------"
test()

