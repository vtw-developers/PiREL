
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]], [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]]
    # output: 3
    # EXPLANATION: In the picture above, the grid on the left is grid1 and the grid on the right is grid2. The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
    ,
    # example 2
    [[[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]], [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]]
    # output: 2
    # EXPLANATION: In the picture above, the grid on the left is grid1 and the grid on the right is grid2. The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countSubIslands 
from typing import *
def f_gold(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    def dfs(i, j):
        ans = grid1[i][j] == 1
        grid2[i][j] = 0
        for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1 and not dfs(x, y):
                ans = False
        return ans
    m, n = len(grid1), len(grid1[0])
    return sum(grid2[i][j] == 1 and dfs(i, j) for i in range(m) for j in range(n))
"-----------------"
test()

