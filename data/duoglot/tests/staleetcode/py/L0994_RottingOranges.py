
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]]
    # output: 4
    ,
    # example 2
    [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]]
    # output: -1
    # EXPLANATION:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    ,
    # example 3
    [[[0, 2]]]
    # output: 0
    # EXPLANATION:  Since there are already no fresh oranges at minute 0, the answer is just 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### orangesRotting 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                cnt += 1
    ans = 0
    while q and cnt:
        ans += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    cnt -= 1
                    grid[x][y] = 2
                    q.append((x, y))
    return ans if cnt == 0 else -1
"-----------------"
test()

