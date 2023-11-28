
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]]
    # output: 8
    # EXPLANATION:  There are 8 negatives number in the matrix.
    ,
    # example 2
    [[[3, 2], [1, 0]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countNegatives 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    i, j = m - 1, 0
    ans = 0
    while i >= 0 and j < n:
        if grid[i][j] < 0:
            ans += n - j
            i -= 1
        else:
            j += 1
    return ans
"-----------------"
test()

