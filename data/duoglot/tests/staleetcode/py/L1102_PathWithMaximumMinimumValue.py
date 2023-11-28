
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[5, 4, 5], [1, 2, 6], [7, 4, 6]]]
    # output: 4
    # EXPLANATION:  The path with the maximum score is highlighted in yellow.
    ,
    # example 2
    [[[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]]
    # output: 2
    ,
    # example 3
    [[[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumMinimumPath 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    m, n = len(grid), len(grid[0])
    p = list(range(m * n))
    ans = min(grid[0][0], grid[-1][-1])
    vis = {(0, 0), (m - 1, n - 1)}
    scores = [[grid[i][j], i, j] for i in range(m) for j in range(n)]
    scores.sort()
    while find(0) != find(m * n - 1):
        score, i, j = scores.pop()
        ans = min(ans, score)
        vis.add((i, j))
        for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and (x, y) in vis:
                p[find(x * n + y)] = find(i * n + j)
    return ans
"-----------------"
test()

