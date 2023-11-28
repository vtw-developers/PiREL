
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]]
    # output: 12
    # EXPLANATION:  One possible way is : left -> down -> left -> down -> right -> down -> right. The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
    ,
    # example 2
    [[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]]
    # output: -1
    # EXPLANATION:  There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
    ,
    # example 3
    [[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1]]
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
def f_gold(maze: List[List[int]], start: List[int], destination: List[int]
) -> int:
    m, n = len(maze), len(maze[0])
    rs, cs = start
    rd, cd = destination
    dist = [[float('inf')] * n for _ in range(m)]
    dist[rs][cs] = 0
    q = deque([(rs, cs)])
    while q:
        i, j = q.popleft()
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y, step = i, j, dist[i][j]
            while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] == 0:
                x, y, step = x + a, y + b, step + 1
            if step < dist[x][y]:
                dist[x][y] = step
                q.append((x, y))
    return -1 if dist[rd][cd] == float('inf') else dist[rd][cd]
"-----------------"
test()

