
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 6, 0], [5, 8, 7], [0, 9, 0]]]
    # output: 24
    # EXPLANATION:  [[0,6,0],  [5,8,7],  [0,9,0]] Path to get the maximum gold, 9 -> 8 -> 7.
    ,
    # example 2
    [[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]]
    # output: 28
    # EXPLANATION:  [[1,0,7],  [2,0,6],  [3,4,5],  [0,3,0],  [9,0,20]] Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getMaximumGold 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n and grid[i][j]):
            return 0
        t = grid[i][j]
        grid[i][j] = 0
        ans = t + max(
            dfs(i + a, j + b) for a, b in [[0, 1], [0, -1], [-1, 0], [1, 0]]
        )
        grid[i][j] = t
        return ans
    m, n = len(grid), len(grid[0])
    return max(dfs(i, j) for i in range(m) for j in range(n))
"-----------------"
test()

