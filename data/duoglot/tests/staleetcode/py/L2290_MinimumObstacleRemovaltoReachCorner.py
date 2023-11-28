
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, 1], [1, 1, 0], [1, 1, 0]]]
    # output: 2
    # EXPLANATION:  We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2). It can be shown that we need to remove at least 2 obstacles, so we return 2. Note that there may be other ways to remove 2 obstacles to create a path.
    ,
    # example 2
    [[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]]
    # output: 0
    # EXPLANATION:  We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumObstacles 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    q = deque([(0, 0, 0)])
    m, n = len(grid), len(grid[0])
    vis = set()
    while q:
        i, j, k = q.popleft()
        if i == m - 1 and j == n - 1:
            return k
        if (i, j) in vis:
            continue
        vis.add((i, j))
        for a, b in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 0:
                    q.appendleft((x, y, k))
                else:
                    q.append((x, y, k + 1))
    return 0
"-----------------"
test()

