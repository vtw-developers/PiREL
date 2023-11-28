
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]]
    # output: 2
    # EXPLANATION:   Islands in gray are closed because they are completely surrounded by water (group of 1s).
    ,
    # example 2
    [[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]]
    # output: 1
    ,
    # example 3
    [[[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### closedIsland 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    p = list(range(m * n))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                continue
            idx = i * n + j
            if i < m - 1 and grid[i + 1][j] == 0:
                p[find(idx)] = find((i + 1) * n + j)
            if j < n - 1 and grid[i][j + 1] == 0:
                p[find(idx)] = find(i * n + j + 1)
    s = [0] * (m * n)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                s[find(i * n + j)] = 1
    for i in range(m):
        for j in range(n):
            root = find(i * n + j)
            if not s[root]:
                continue
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                s[root] = 0
    return sum(s)
"-----------------"
test()

