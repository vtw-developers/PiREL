
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 15, 20]]
    # output: 15
    # EXPLANATION:  You will start at index 1. - Pay 15 and climb two steps to reach the top. The total cost is 15.
    ,
    # example 2
    [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]
    # output: 6
    # EXPLANATION:  You will start at index 0. - Pay 1 and climb two steps to reach index 2. - Pay 1 and climb two steps to reach index 4. - Pay 1 and climb two steps to reach index 6. - Pay 1 and climb one step to reach index 7. - Pay 1 and climb two steps to reach index 9. - Pay 1 and climb one step to reach the top. The total cost is 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minCostClimbingStairs 
from typing import *
def f_gold(cost: List[int]) -> int:
    a = b = 0
    for i in range(1, len(cost)):
        a, b = b, min(a + cost[i - 1], b + cost[i])
    return b
"-----------------"
test()

