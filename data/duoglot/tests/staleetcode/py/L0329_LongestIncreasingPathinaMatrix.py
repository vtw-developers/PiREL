
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[9, 9, 4], [6, 6, 8], [2, 1, 1]]]
    # output: 4
    # EXPLANATION:  The longest increasing path is <code>[1, 2, 6, 9]</code>.
    ,
    # example 2
    [[[3, 4, 5], [3, 2, 6], [2, 2, 1]]]
    # output: 4
    # EXPLANATION: The longest increasing path is <code>[3, 4, 5, 6]</code>. Moving diagonally is not allowed.
    ,
    # example 3
    [[[1]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestIncreasingPath 
def cache(f): return f
from typing import *
def f_gold(matrix: List[List[int]]) -> int:
    @cache
    def dfs(i, j):
        ans = 1
        for a, b in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                ans = max(ans, dfs(x, y) + 1)
        return ans
    m, n = len(matrix), len(matrix[0])
    return max(dfs(i, j) for i in range(m) for j in range(n))
"-----------------"
test()

