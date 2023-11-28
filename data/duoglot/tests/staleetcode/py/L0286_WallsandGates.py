
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]]
    # output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    ,
    # example 2
    [[[-1]]]
    # output: [[-1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### wallsAndGates 
import math
from math import inf
from collections import deque
from typing import *
def f_gold(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    m, n = len(rooms), len(rooms[0])
    inf = 2**31 - 1
    q = deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
    d = 0
    while q:
        d += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == inf:
                    rooms[x][y] = d
                    q.append((x, y))
"-----------------"
test()

