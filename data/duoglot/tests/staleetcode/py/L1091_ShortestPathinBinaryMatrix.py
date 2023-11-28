
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [1, 0]]]
    # output: 2
    ,
    # example 2
    [[[0, 0, 0], [1, 1, 0], [1, 1, 0]]]
    # output: 4
    ,
    # example 3
    [[[1, 0, 0], [1, 1, 0], [1, 1, 0]]]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestPathBinaryMatrix 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    if grid[0][0]:
        return -1
    n = len(grid)
    q = deque([(0, 0)])
    grid[0][0] = 1
    ans = 0
    while q:
        ans += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == (n - 1, n - 1):
                return ans
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        q.append((x, y))
                        grid[x][y] = 1
    return -1
"-----------------"
test()

