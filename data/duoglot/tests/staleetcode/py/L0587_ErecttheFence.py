
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]]
    # output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
    ,
    # example 2
    [[[1, 2], [2, 2], [4, 2]]]
    # output: [[4,2],[2,2],[1,2]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### outerTrees 
from typing import *
def f_gold(trees: List[List[int]]) -> List[List[int]]:
    def cross(i, j, k):
        a, b, c = trees[i], trees[j], trees[k]
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
    n = len(trees)
    if n < 4:
        return trees
    trees.sort()
    vis = [False] * n
    stk = [0]
    for i in range(1, n):
        while len(stk) > 1 and cross(stk[-2], stk[-1], i) < 0:
            vis[stk.pop()] = False
        vis[i] = True
        stk.append(i)
    m = len(stk)
    for i in range(n - 2, -1, -1):
        if vis[i]:
            continue
        while len(stk) > m and cross(stk[-2], stk[-1], i) < 0:
            stk.pop()
        stk.append(i)
    stk.pop()
    return [trees[i] for i in stk]
"-----------------"
test()

