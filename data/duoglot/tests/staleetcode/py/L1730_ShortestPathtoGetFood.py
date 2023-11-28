
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"], ["X", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X"]]]
    # output: 3
    # EXPLANATION:  It takes 3 steps to reach the food.
    ,
    # example 2
    [[["X", "X", "X", "X", "X"], ["X", "*", "X", "O", "X"], ["X", "O", "X", "#", "X"], ["X", "X", "X", "X", "X"]]]
    # output: -1
    # EXPLANATION:  It is not possible to reach the food.
    ,
    # example 3
    [[["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"], ["X", "O", "O", "X", "O", "O", "X", "X"], ["X", "O", "O", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"]]]
    # output: 6
    # EXPLANATION:  There can be multiple food cells. It only takes 6 steps to reach the bottom food.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getFood 
from collections import deque
from typing import *
def f_gold(grid: List[List[str]]) -> int:
    def pos():
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    return i, j
    m, n = len(grid), len(grid[0])
    q = deque([pos()])
    ans = 0
    while q:
        ans += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == '#':
                        return ans
                    if grid[x][y] == 'O':
                        grid[x][y] = 'X'
                        q.append((x, y))
    return -1
"-----------------"
test()

