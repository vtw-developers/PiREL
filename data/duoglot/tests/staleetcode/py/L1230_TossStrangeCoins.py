
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0.4], 1]
    # output: 0.40000
    ,
    # example 2
    [[0.5, 0.5, 0.5, 0.5, 0.5], 0]
    # output: 0.03125
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### probabilityOfHeads 
from typing import *
def f_gold(prob: List[float], target: int) -> float:
    dp = [0] * (target + 1)
    dp[0] = 1
    for v in prob:
        for j in range(target, -1, -1):
            dp[j] *= 1 - v
            if j >= 1:
                dp[j] += dp[j - 1] * v
    return dp[-1]
"-----------------"
test()

