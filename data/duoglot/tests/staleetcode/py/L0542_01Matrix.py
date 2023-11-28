
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]]
    # output: [[0,0,0],[0,1,0],[0,0,0]]
    ,
    # example 2
    [[[0, 0, 0], [0, 1, 0], [1, 1, 1]]]
    # output: [[0,0,0],[0,1,0],[1,2,1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### updateMatrix 
from collections import deque
from typing import *
def f_gold(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    ans = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                ans[i][j] = 0
                q.append((i, j))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        i, j = q.popleft()
        for a, b in dirs:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                ans[x][y] = ans[i][j] + 1
                q.append((x, y))
    return ans
"-----------------"
test()

