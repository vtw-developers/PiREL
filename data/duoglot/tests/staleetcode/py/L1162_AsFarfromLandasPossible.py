
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 1], [0, 0, 0], [1, 0, 1]]]
    # output: 2
    # EXPLANATION:  The cell (1, 1) is as far as possible from all the land with distance 2.
    ,
    # example 2
    [[[1, 0, 0], [0, 0, 0], [0, 0, 0]]]
    # output: 4
    # EXPLANATION:  The cell (2, 2) is as far as possible from all the land with distance 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxDistance 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    n = len(grid)
    q = deque([(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1])
    ans = -1
    valid = False
    while q:
        ans += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x, y = i + a, b + j
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    valid = True
                    grid[x][y] = 1
                    q.append((x, y))
    return ans if valid else -1
"-----------------"
test()

