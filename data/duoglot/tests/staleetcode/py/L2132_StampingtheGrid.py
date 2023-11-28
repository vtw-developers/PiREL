
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 4, 3]
    # output: true
    # EXPLANATION:  We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.
    ,
    # example 2
    [[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 2, 2]
    # output: false
    # EXPLANATION:  There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### possibleToStamp 
from typing import *
def f_gold(grid: List[List[int]], stampHeight: int, stampWidth: int
) -> bool:
    m, n = len(grid), len(grid[0])
    s = [[0] * (n + 1) for _ in range(m + 1)]
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v
    d = [[0] * (n + 1) for _ in range(m + 1)]
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 0:
                x, y = i + stampHeight, j + stampWidth
                if x <= m and y <= n and s[x][y] - s[x][j] - s[i][y] + s[i][j] == 0:
                    d[i][j] += 1
                    d[i][y] -= 1
                    d[x][j] -= 1
                    d[x][y] += 1
    cnt = [[0] * (n + 1) for _ in range(m + 1)]
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            cnt[i + 1][j + 1] = cnt[i + 1][j] + cnt[i][j + 1] - cnt[i][j] + d[i][j]
            if v == 0 and cnt[i + 1][j + 1] == 0:
                return False
    return True
"-----------------"
test()

