
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]]
    # output: 7
    # EXPLANATION:  Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2). The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
    ,
    # example 2
    [[[1, 0]]]
    # output: 1
    ,
    # example 3
    [[[1]]]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestDistance 
import math
from math import inf
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    total = 0
    cnt = [[0] * n for _ in range(m)]
    dist = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                total += 1
                q.append((i, j))
                d = 0
                vis = set()
                while q:
                    d += 1
                    for _ in range(len(q)):
                        r, c = q.popleft()
                        for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            x, y = r + a, c + b
                            if (
                                0 <= x < m
                                and 0 <= y < n
                                and grid[x][y] == 0
                                and (x, y) not in vis
                            ):
                                cnt[x][y] += 1
                                dist[x][y] += d
                                q.append((x, y))
                                vis.add((x, y))
    ans = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and cnt[i][j] == total:
                ans = min(ans, dist[i][j])
    return -1 if ans == float('inf') else ans
"-----------------"
test()

