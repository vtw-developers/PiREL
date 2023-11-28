
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]]
    # output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    ,
    # example 2
    [[[2, 1], [1, 2]]]
    # output: [[0,0],[0,1],[1,0],[1,1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### pacificAtlantic 
from collections import deque
from typing import *
def f_gold(heights: List[List[int]]) -> List[List[int]]:
    def bfs(q, vis):
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                    x, y = i + a, j + b
                    if (
                        0 <= x < m
                        and 0 <= y < n
                        and (x, y) not in vis
                        and heights[x][y] >= heights[i][j]
                    ):
                        vis.add((x, y))
                        q.append((x, y))
    m, n = len(heights), len(heights[0])
    vis1, vis2 = set(), set()
    q1 = deque()
    q2 = deque()
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                vis1.add((i, j))
                q1.append((i, j))
            if i == m - 1 or j == n - 1:
                vis2.add((i, j))
                q2.append((i, j))
    bfs(q1, vis1)
    bfs(q2, vis2)
    return [
        (i, j)
        for i in range(m)
        for j in range(n)
        if (i, j) in vis1 and (i, j) in vis2
    ]
"-----------------"
test()

