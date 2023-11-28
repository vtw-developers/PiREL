
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]]
    # output: 20
    # EXPLANATION:   <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1584.Min%20Cost%20to%20Connect%20All%20Points/images/c.png" style="width: 214px; height: 268px;" /> We can connect the points as shown above to get the minimum cost of 20. Notice that there is a unique path between every pair of points.
    ,
    # example 2
    [[[3, 12], [-2, 5], [-4, 1]]]
    # output: 18
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minCostConnectPoints 
from typing import *
def f_gold(points: List[List[int]]) -> int:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    g = []
    n = len(points)
    for i, (x1, y1) in enumerate(points):
        for j in range(i + 1, n):
            x2, y2 = points[j]
            g.append((abs(x1 - x2) + abs(y1 - y2), i, j))
    g.sort()
    p = list(range(n))
    ans = 0
    for cost, i, j in g:
        if find(i) == find(j):
            continue
        p[find(i)] = find(j)
        n -= 1
        ans += cost
        if n == 1:
            return ans
    return 0
"-----------------"
test()

