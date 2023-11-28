
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[" /", "/ "]]
    # output: 2
    ,
    # example 2
    [[" /", "  "]]
    # output: 1
    ,
    # example 3
    [["/\\", "\\/"]]
    # output: 5
    # EXPLANATION: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### regionsBySlashes 
from typing import *
def f_gold(grid: List[str]) -> int:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            p[pa] = pb
            nonlocal size
            size -= 1
    n = len(grid)
    size = n * n * 4
    p = list(range(size))
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            k = i * n + j
            if i < n - 1:
                union(4 * k + 2, (k + n) * 4)
            if j < n - 1:
                union(4 * k + 1, (k + 1) * 4 + 3)
            if v == '/':
                union(4 * k, 4 * k + 3)
                union(4 * k + 1, 4 * k + 2)
            elif v == '\\':
                union(4 * k, 4 * k + 1)
                union(4 * k + 2, 4 * k + 3)
            else:
                union(4 * k, 4 * k + 1)
                union(4 * k + 1, 4 * k + 2)
                union(4 * k + 2, 4 * k + 3)
    return size
"-----------------"
test()

