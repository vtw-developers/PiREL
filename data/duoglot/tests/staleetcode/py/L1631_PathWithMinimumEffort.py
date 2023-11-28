
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 2], [3, 8, 2], [5, 3, 5]]]
    # output: 2
    # EXPLANATION:  The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.  This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
    ,
    # example 2
    [[[1, 2, 3], [3, 8, 4], [5, 3, 5]]]
    # output: 1
    # EXPLANATION:  The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
    ,
    # example 3
    [[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]]
    # output: 0
    # EXPLANATION:  This route does not require any effort.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumEffortPath 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(heights: List[List[int]]) -> int:
    INF = 0x3F3F3F3F
    m, n = len(heights), len(heights[0])
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = 0
    dirs = [-1, 0, 1, 0, -1]
    q = [(0, 0, 0)]
    while q:
        t, i, j = heappop(q)
        for k in range(4):
            x, y = i + dirs[k], j + dirs[k + 1]
            if (
                0 <= x < m
                and 0 <= y < n
                and max(t, abs(heights[x][y] - heights[i][j])) < dist[x][y]
            ):
                dist[x][y] = max(t, abs(heights[x][y] - heights[i][j]))
                heappush(q, (dist[x][y], x, y))
    return dist[-1][-1]
"-----------------"
test()

