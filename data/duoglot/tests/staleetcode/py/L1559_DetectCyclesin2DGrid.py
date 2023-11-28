
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]]
    # output: true
    # EXPLANATION: There are two valid cycles shown in different colors in the image below: <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/11.png" style="width: 225px; height: 163px;" />
    ,
    # example 2
    [[["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]]
    # output: true
    # EXPLANATION: There is only one valid cycle highlighted in the image below: <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/2.png" style="width: 229px; height: 157px;" />
    ,
    # example 3
    [[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### containsCycle 
from typing import *
def f_gold(grid: List[List[str]]) -> bool:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    m, n = len(grid), len(grid[0])
    p = list(range(m * n))
    for i in range(m):
        for j in range(n):
            for a, b in [[0, 1], [1, 0]]:
                x, y = i + a, j + b
                if x < m and y < n and grid[x][y] == grid[i][j]:
                    if find(x * n + y) == find(i * n + j):
                        return True
                    p[find(x * n + y)] = find(i * n + j)
    return False
"-----------------"
test()

