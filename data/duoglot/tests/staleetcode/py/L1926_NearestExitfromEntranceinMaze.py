
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]]
    # output: 1
    # EXPLANATION:  There are 3 exits in this maze at [1,0], [0,2], and [2,3]. Initially, you are at the entrance cell [1,2]. - You can reach [1,0] by moving 2 steps left. - You can reach [0,2] by moving 1 step up. It is impossible to reach [2,3] from the entrance. Thus, the nearest exit is [0,2], which is 1 step away.
    ,
    # example 2
    [[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]]
    # output: 2
    # EXPLANATION:  There is 1 exit in this maze at [1,2]. [1,0] does not count as an exit since it is the entrance cell. Initially, you are at the entrance cell [1,0]. - You can reach [1,2] by moving 2 steps right. Thus, the nearest exit is [1,2], which is 2 steps away.
    ,
    # example 3
    [[[".", "+"]], [0, 0]]
    # output: -1
    # EXPLANATION:  There are no exits in this maze.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### nearestExit 
from collections import deque
from typing import *
def f_gold(maze: List[List[str]], entrance: List[int]) -> int:
    m, n = len(maze), len(maze[0])
    i, j = entrance
    q = deque([(i, j)])
    maze[i][j] = '+'
    ans = 0
    while q:
        ans += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return ans
                    q.append((x, y))
                    maze[x][y] = '+'
    return -1
"-----------------"
test()

