
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [0, 0, 4], [7, 6, 5]]]
    # output: 6
    # EXPLANATION:  Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
    ,
    # example 2
    [[[1, 2, 3], [0, 0, 0], [7, 6, 5]]]
    # output: -1
    # EXPLANATION:  The trees in the bottom row cannot be accessed as the middle row is blocked.
    ,
    # example 3
    [[[2, 3, 4], [0, 0, 5], [8, 7, 6]]]
    # output: 6
    # EXPLANATION:  You can follow the same path as Example 1 to cut off all the trees. Note that you can cut off the first tree at (0, 0) before making any steps.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### cutOffTree 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(forest: List[List[int]]) -> int:
    def f(i, j, x, y):
        return abs(i - x) + abs(j - y)
    def bfs(i, j, x, y):
        q = [(f(i, j, x, y), i, j)]
        dist = {i * n + j: 0}
        while q:
            _, i, j = heappop(q)
            step = dist[i * n + j]
            if (i, j) == (x, y):
                return step
            for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                c, d = i + a, j + b
                if 0 <= c < m and 0 <= d < n and forest[c][d] > 0:
                    if c * n + d not in dist or dist[c * n + d] > step + 1:
                        dist[c * n + d] = step + 1
                        heappush(q, (dist[c * n + d] + f(c, d, x, y), c, d))
        return -1
    m, n = len(forest), len(forest[0])
    trees = [
        (forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1
    ]
    trees.sort()
    i = j = 0
    ans = 0
    for _, x, y in trees:
        t = bfs(i, j, x, y)
        if t == -1:
            return -1
        ans += t
        i, j = x, y
    return ans
"-----------------"
test()

