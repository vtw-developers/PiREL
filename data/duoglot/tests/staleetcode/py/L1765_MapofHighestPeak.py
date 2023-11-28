
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [0, 0]]]
    # output: [[1,0],[2,1]]
    # EXPLANATION:  The image shows the assigned heights of each cell. The blue cell is the water cell, and the green cells are the land cells.
    ,
    # example 2
    [[[0, 0, 1], [1, 0, 0], [0, 0, 0]]]
    # output: [[1,1,0],[0,1,1],[1,2,2]]
    # EXPLANATION:  A height of 2 is the maximum possible height of any assignment. Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### highestPeak 
from collections import deque
from typing import *
def f_gold(isWater: List[List[int]]) -> List[List[int]]:
    m, n = len(isWater), len(isWater[0])
    ans = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                ans[i][j] = 0
                q.append((i, j))
    while q:
        i, j = q.popleft()
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                ans[x][y] = ans[i][j] + 1
                q.append((x, y))
    return ans
"-----------------"
test()

