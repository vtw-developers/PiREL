
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0], [0, 1]]]
    # output: 3
    # EXPLANATION:  Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
    ,
    # example 2
    [[[1, 1], [1, 0]]]
    # output: 4
    # EXPLANATION: Change the 0 to 1 and make the island bigger, only one island with area = 4.
    ,
    # example 3
    [[[1, 1], [1, 1]]]
    # output: 4
    # EXPLANATION:  Can't change any 0 to 1, only one island with area = 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestIsland 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    n = len(grid)
    p = list(range(n * n))
    size = [1] * (n * n)
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            size[pb] += size[pa]
            p[pa] = pb
    def check(i, j):
        return 0 <= i < n and 0 <= j < n and grid[i][j] == 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                for x, y in [[1, 0], [0, 1]]:
                    if check(i + x, j + y):
                        union(i * n + j, (i + x) * n + j + y)
    res = max(size)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                t = 1
                s = set()
                for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if check(i + x, j + y):
                        root = find((i + x) * n + j + y)
                        if root not in s:
                            t += size[root]
                            s.add(root)
                res = max(res, t)
    return res
"-----------------"
test()

