
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 5, 4], [1, 5, 1]]]
    # output: 4
    # EXPLANATION:  The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue. The cells visited by the first robot are set to 0. The second robot will collect 0 + 0 + 4 + 0 = 4 points.
    ,
    # example 2
    [[[3, 3, 1], [8, 5, 2]]]
    # output: 4
    # EXPLANATION:  The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue. The cells visited by the first robot are set to 0. The second robot will collect 0 + 3 + 1 + 0 = 4 points.
    ,
    # example 3
    [[[1, 3, 1, 15], [1, 3, 3, 1]]]
    # output: 7
    # EXPLANATION: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue. The cells visited by the first robot are set to 0. The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### gridGame 
import math
from math import inf
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    ans = inf
    s1, s2 = sum(grid[0]), 0
    for j, v in enumerate(grid[0]):
        s1 -= v
        ans = min(ans, max(s1, s2))
        s2 += grid[1][j]
    return ans
"-----------------"
test()

