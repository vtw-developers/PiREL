
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]]
    # output: 10
    # EXPLANATION:  There are 2 contaminated regions. On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is: <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus12edited-grid.jpg" style="width: 500px; height: 257px;" /> On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained. <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus13edited-grid.jpg" style="width: 500px; height: 261px;" />
    ,
    # example 2
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
    # output: 4
    # EXPLANATION:  Even though there is only one cell saved, there are 4 walls built. Notice that walls are only built on the shared boundary of two different cells.
    ,
    # example 3
    [[[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]]]
    # output: 13
    # EXPLANATION:  The region on the left only builds two new walls.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### containVirus 
from typing import *
def f_gold(isInfected: List[List[int]]) -> int:
    def dfs(i, j):
        vis[i][j] = True
        areas[-1].add((i, j))
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n:
                if isInfected[x][y] == 1 and not vis[x][y]:
                    dfs(x, y)
                elif isInfected[x][y] == 0:
                    c[-1] += 1
                    boundaries[-1].add((x, y))
    m, n = len(isInfected), len(isInfected[0])
    ans = 0
    while 1:
        vis = [[False] * n for _ in range(m)]
        areas = []
        c = []
        boundaries = []
        for i, row in enumerate(isInfected):
            for j, v in enumerate(row):
                if v == 1 and not vis[i][j]:
                    areas.append(set())
                    boundaries.append(set())
                    c.append(0)
                    dfs(i, j)
        if not areas:
            break
        idx = boundaries.index(max(boundaries, key=len))
        ans += c[idx]
        for k, area in enumerate(areas):
            if k == idx:
                for i, j in area:
                    isInfected[i][j] = -1
            else:
                for i, j in area:
                    for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                        x, y = i + a, j + b
                        if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 0:
                            isInfected[x][y] = 1
    return ans
"-----------------"
test()

