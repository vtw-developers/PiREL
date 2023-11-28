
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[40, 10], [30, 20]], 1]
    # output: [[10,20],[40,30]]
    # EXPLANATION:  The figures above represent the grid at every state.
    ,
    # example 2
    [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2]
    # output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
    # EXPLANATION:  The figures above represent the grid at every state.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rotateGrid 
from typing import *
def f_gold(grid: List[List[int]], k: int) -> List[List[int]]:
    def rotate(grid, s1, e1, s2, e2, k):
        t = []
        for j in range(e2, e1, -1):
            t.append(grid[s1][j])
        for i in range(s1, s2):
            t.append(grid[i][e1])
        for j in range(e1, e2):
            t.append(grid[s2][j])
        for i in range(s2, s1, -1):
            t.append(grid[i][e2])
        k %= len(t)
        t = t[-k:] + t[:-k]
        k = 0
        for j in range(e2, e1, -1):
            grid[s1][j] = t[k]
            k += 1
        for i in range(s1, s2):
            grid[i][e1] = t[k]
            k += 1
        for j in range(e1, e2):
            grid[s2][j] = t[k]
            k += 1
        for i in range(s2, s1, -1):
            grid[i][e2] = t[k]
            k += 1
    m, n = len(grid), len(grid[0])
    s1 = e1 = 0
    s2, e2 = m - 1, n - 1
    while s1 <= s2 and e1 <= e2:
        rotate(grid, s1, e1, s2, e2, k)
        s1 += 1
        e1 += 1
        s2 -= 1
        e2 -= 1
    return grid
"-----------------"
test()

