
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]]
    # output: [2]
    # EXPLANATION: Starting with the grid: [[1,0,0,0],  [<u>1</u>,1,1,0]] We erase the underlined brick at (1,0), resulting in the grid: [[1,0,0,0],  [0,<u>1</u>,<u>1</u>,0]] The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is: [[1,0,0,0],  [0,0,0,0]] Hence the result is [2].
    ,
    # example 2
    [[[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]]
    # output: [0,0]
    # EXPLANATION: Starting with the grid: [[1,0,0,0],  [1,<u>1</u>,0,0]] We erase the underlined brick at (1,1), resulting in the grid: [[1,0,0,0],  [1,0,0,0]] All remaining bricks are still stable, so no bricks fall. The grid remains the same: [[1,0,0,0],  [<u>1</u>,0,0,0]] Next, we erase the underlined brick at (1,0), resulting in the grid: [[1,0,0,0],  [0,0,0,0]] Once again, all remaining bricks are still stable, so no bricks fall. Hence the result is [0,0].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hitBricks 
from copy import deepcopy
from typing import *
def f_gold(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            size[pb] += size[pa]
            p[pa] = pb
    m, n = len(grid), len(grid[0])
    p = list(range(m * n + 1))
    size = [1] * len(p)
    g = deepcopy(grid)
    for i, j in hits:
        g[i][j] = 0
    for j in range(n):
        if g[0][j] == 1:
            union(j, m * n)
    for i in range(1, m):
        for j in range(n):
            if g[i][j] == 0:
                continue
            if g[i - 1][j] == 1:
                union(i * n + j, (i - 1) * n + j)
            if j > 0 and g[i][j - 1] == 1:
                union(i * n + j, i * n + j - 1)
    ans = []
    for i, j in hits[::-1]:
        if grid[i][j] == 0:
            ans.append(0)
            continue
        g[i][j] = 1
        prev = size[find(m * n)]
        if i == 0:
            union(j, m * n)
        for a, b in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and g[x][y] == 1:
                union(i * n + j, x * n + y)
        curr = size[find(m * n)]
        ans.append(max(0, curr - prev - 1))
    return ans[::-1]
"-----------------"
test()

