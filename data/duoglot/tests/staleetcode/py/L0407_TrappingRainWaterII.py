
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]]
    # output: 4
    # EXPLANATION:  After the rain, water is trapped between the blocks. We have two small ponds 1 and 3 units trapped. The total volume of water trapped is 4.
    ,
    # example 2
    [[[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]]
    # output: 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### trapRainWater 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(heightMap: List[List[int]]) -> int:
    m, n = len(heightMap), len(heightMap[0])
    vis = [[False] * n for _ in range(m)]
    pq = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heappush(pq, (heightMap[i][j], i, j))
                vis[i][j] = True
    ans = 0
    while pq:
        e = heappop(pq)
        for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            i, j = e[1] + x, e[2] + y
            if i >= 0 and i < m and j >= 0 and j < n and not vis[i][j]:
                if heightMap[i][j] < e[0]:
                    ans += e[0] - heightMap[i][j]
                vis[i][j] = True
                heappush(pq, (max(heightMap[i][j], e[0]), i, j))
    return ans
"-----------------"
test()

