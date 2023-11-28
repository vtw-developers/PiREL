
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[5, 3], [4, 0], [2, 1]], [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]]
    # output: 17
    # EXPLANATION: The path with the minimum possible cost is the path 5 -> 0 -> 1. - The sum of the values of cells visited is 5 + 0 + 1 = 6. - The cost of moving from 5 to 0 is 3. - The cost of moving from 0 to 1 is 8. So the total cost of the path is 6 + 3 + 8 = 17.
    ,
    # example 2
    [[[5, 1, 2], [4, 0, 3]], [[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]]]
    # output: 6
    # EXPLANATION:  The path with the minimum possible cost is the path 2 -> 3. - The sum of the values of cells visited is 2 + 3 = 5. - The cost of moving from 2 to 3 is 1. So the total cost of this path is 5 + 1 = 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minPathCost 
import math
from math import inf
from typing import *
def f_gold(grid: List[List[int]], moveCost: List[List[int]]) -> int:
    n = len(grid[0])
    f = [0] * n
    for i, row in enumerate(grid):
        g = [0] * n
        for j, v in enumerate(row):
            g[j] = v
            t = inf
            if i:
                for k, x in enumerate(grid[i - 1]):
                    t = min(t, f[k] + moveCost[x][j])
            if t != inf:
                g[j] += t
        f = g
    return min(f)
"-----------------"
test()

