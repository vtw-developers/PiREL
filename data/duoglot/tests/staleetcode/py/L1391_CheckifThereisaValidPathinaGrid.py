
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 4, 3], [6, 5, 2]]]
    # output: true
    # EXPLANATION:  As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
    ,
    # example 2
    [[[1, 2, 1], [1, 2, 1]]]
    # output: false
    # EXPLANATION:  As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
    ,
    # example 3
    [[[1, 1, 2]]]
    # output: false
    # EXPLANATION:  You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hasValidPath 
from typing import *
def f_gold(grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    p = list(range(m * n))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def left(i, j):
        if j > 0 and grid[i][j - 1] in (1, 4, 6):
            p[find(i * n + j)] = find(i * n + j - 1)
    def right(i, j):
        if j < n - 1 and grid[i][j + 1] in (1, 3, 5):
            p[find(i * n + j)] = find(i * n + j + 1)
    def up(i, j):
        if i > 0 and grid[i - 1][j] in (2, 3, 4):
            p[find(i * n + j)] = find((i - 1) * n + j)
    def down(i, j):
        if i < m - 1 and grid[i + 1][j] in (2, 5, 6):
            p[find(i * n + j)] = find((i + 1) * n + j)
    for i in range(m):
        for j in range(n):
            e = grid[i][j]
            if e == 1:
                left(i, j)
                right(i, j)
            elif e == 2:
                up(i, j)
                down(i, j)
            elif e == 3:
                left(i, j)
                down(i, j)
            elif e == 4:
                right(i, j)
                down(i, j)
            elif e == 5:
                left(i, j)
                up(i, j)
            else:
                right(i, j)
                up(i, j)
    return find(0) == find(m * n - 1)
"-----------------"
test()

