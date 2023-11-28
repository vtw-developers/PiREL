
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 1, 0], [0, 2, 0, 0, 1, 2, 0], [0, 0, 2, 2, 2, 0, 2], [0, 0, 0, 0, 0, 0, 0]]]
    # output: 3
    # EXPLANATION:  The figure above shows the scenario where you stay in the initial position for 3 minutes. You will still be able to safely reach the safehouse. Staying for more than 3 minutes will not allow you to safely reach the safehouse.
    ,
    # example 2
    [[[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]]]
    # output: -1
    # EXPLANATION:  The figure above shows the scenario where you immediately move towards the safehouse. Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse. Thus, -1 is returned.
    ,
    # example 3
    [[[0, 0, 0], [2, 2, 0], [1, 2, 0]]]
    # output: 1000000000
    # EXPLANATION:  The figure above shows the initial grid. Notice that the fire is contained by walls and you will always be able to safely reach the safehouse. Thus, 10<sup>9</sup> is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumMinutes 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    def spread(fire, q):
        nf = deque()
        while q:
            i, j = q.popleft()
            for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and not fire[x][y] and grid[x][y] == 0:
                    fire[x][y] = True
                    nf.append((x, y))
        return nf
    def check(t):
        fire = [[False] * n for _ in range(m)]
        f = deque()
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    fire[i][j] = True
                    f.append((i, j))
        while t and f:
            f = spread(fire, f)
            t -= 1
        if fire[0][0]:
            return False
        q = deque([(0, 0)])
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if fire[i][j]:
                    continue
                for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    x, y = i + a, j + b
                    if (
                        0 <= x < m
                        and 0 <= y < n
                        and not fire[x][y]
                        and not vis[x][y]
                        and grid[x][y] == 0
                    ):
                        if x == m - 1 and y == n - 1:
                            return True
                        vis[x][y] = True
                        q.append((x, y))
            f = spread(fire, f)
        return False
    m, n = len(grid), len(grid[0])
    left, right = -1, m * n
    while left < right:
        mid = (left + right + 1) >> 1
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return int(1e9) if left == m * n else left
"-----------------"
test()

