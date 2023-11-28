
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1]]
    # output: "lul"
    # EXPLANATION:  There are two shortest ways for the ball to drop into the hole. The first way is left -> up -> left, represented by "lul". The second way is up -> left, represented by 'ul'. Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".
    ,
    # example 2
    [[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [3, 0]]
    # output: "impossible"
    # EXPLANATION:  The ball cannot reach the hole.
    ,
    # example 3
    [[[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1]], [0, 4], [3, 5]]
    # output: "dldr"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findShortestWay 
import math
from math import inf
from collections import deque
from typing import *
def f_gold(maze: List[List[int]], ball: List[int], hole: List[int]
) -> str:
    m, n = len(maze), len(maze[0])
    r, c = ball
    rh, ch = hole
    q = deque([(r, c)])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[r][c] = 0
    path = [[None] * n for _ in range(m)]
    path[r][c] = ''
    while q:
        i, j = q.popleft()
        for a, b, d in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
            x, y, step = i, j, dist[i][j]
            while (
                0 <= x + a < m
                and 0 <= y + b < n
                and maze[x + a][y + b] == 0
                and (x != rh or y != ch)
            ):
                x, y = x + a, y + b
                step += 1
            if dist[x][y] > step or (
                dist[x][y] == step and path[i][j] + d < path[x][y]
            ):
                dist[x][y] = step
                path[x][y] = path[i][j] + d
                if x != rh or y != ch:
                    q.append((x, y))
    return path[rh][ch] or 'impossible'
"-----------------"
test()

