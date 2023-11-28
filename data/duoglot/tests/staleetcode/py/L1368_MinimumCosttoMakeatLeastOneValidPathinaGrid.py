
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]]
    # output: 3
    # EXPLANATION:  You will start at point (0, 0). The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3) The total cost = 3.
    ,
    # example 2
    [[[1, 1, 3], [3, 2, 2], [1, 1, 4]]]
    # output: 0
    # EXPLANATION:  You can follow the path from (0, 0) to (2, 2).
    ,
    # example 3
    [[[1, 2], [4, 3]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minCost 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dirs = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque([(0, 0, 0)])
    vis = set()
    while q:
        i, j, d = q.popleft()
        if (i, j) in vis:
            continue
        vis.add((i, j))
        if i == m - 1 and j == n - 1:
            return d
        for k in range(1, 5):
            x, y = i + dirs[k][0], j + dirs[k][1]
            if 0 <= x < m and 0 <= y < n:
                if grid[i][j] == k:
                    q.appendleft((x, y, d))
                else:
                    q.append((x, y, d + 1))
    return -1
"-----------------"
test()

