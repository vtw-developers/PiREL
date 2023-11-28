
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]]
    # output: true
    # EXPLANATION:  One possible way is : left -> down -> left -> down -> right -> down -> right.
    ,
    # example 2
    [[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]]
    # output: false
    # EXPLANATION:  There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
    ,
    # example 3
    [[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hasPath 
from collections import deque
from typing import *
def f_gold(maze: List[List[int]], start: List[int], destination: List[int]
) -> bool:
    m, n = len(maze), len(maze[0])
    q = deque([start])
    rs, cs = start
    vis = {(rs, cs)}
    while q:
        i, j = q.popleft()
        for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            x, y = i, j
            while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] == 0:
                x, y = x + a, y + b
            if [x, y] == destination:
                return True
            if (x, y) not in vis:
                vis.add((x, y))
                q.append((x, y))
    return False
"-----------------"
test()

