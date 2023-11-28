
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1]
    # output: 6
    # EXPLANATION:   The shortest path without eliminating any obstacle is 10. The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> <strong>(3,2)</strong> -> (4,2).
    ,
    # example 2
    [[[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1]
    # output: -1
    # EXPLANATION:  We need to eliminate at least two obstacles to find such a walk.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestPath 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    if k >= m + n - 3:
        return m + n - 2
    q = deque([(0, 0, k)])
    vis = {(0, 0, k)}
    ans = 0
    while q:
        ans += 1
        for _ in range(len(q)):
            i, j, k = q.popleft()
            for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    if x == m - 1 and y == n - 1:
                        return ans
                    if grid[x][y] == 0 and (x, y, k) not in vis:
                        q.append((x, y, k))
                        vis.add((x, y, k))
                    if grid[x][y] == 1 and k > 0 and (x, y, k - 1) not in vis:
                        q.append((x, y, k - 1))
                        vis.add((x, y, k - 1))
    return -1
"-----------------"
test()

