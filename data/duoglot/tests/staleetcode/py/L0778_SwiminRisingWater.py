
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 2], [1, 3]]]
    # output: 3
    # EXPLANATION:  At time 0, you are in grid location (0, 0). You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0. You cannot reach point (1, 1) until time 3. When the depth of water is 3, we can swim anywhere inside the grid.
    ,
    # example 2
    [[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]]
    # output: 16
    # EXPLANATION:  The final route is shown. We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### swimInWater 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    n = len(grid)
    p = list(range(n * n))
    hi = [0] * (n * n)
    for i, row in enumerate(grid):
        for j, h in enumerate(row):
            hi[h] = i * n + j
    for t in range(n * n):
        i, j = hi[t] // n, hi[t] % n
        for a, b in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            x, y = i + a, j + b
            if 0 <= x < n and 0 <= y < n and grid[x][y] <= t:
                p[find(x * n + y)] = find(hi[t])
            if find(0) == find(n * n - 1):
                return t
    return -1
"-----------------"
test()

