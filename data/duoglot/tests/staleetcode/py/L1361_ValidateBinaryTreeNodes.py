
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [1, -1, 3, -1], [2, -1, -1, -1]]
    # output: true
    ,
    # example 2
    [4, [1, -1, 3, -1], [2, 3, -1, -1]]
    # output: false
    ,
    # example 3
    [2, [1, 0], [-1, -1]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### validateBinaryTreeNodes 
from typing import *
def f_gold(n: int, leftChild: List[int], rightChild: List[int]
) -> bool:
    p = list(range(n))
    vis = [False] * n
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    for i in range(n):
        l, r = leftChild[i], rightChild[i]
        if l != -1:
            if vis[l] or find(i) == find(l):
                return False
            p[find(i)] = find(l)
            vis[l] = True
            n -= 1
        if r != -1:
            if vis[r] or find(i) == find(r):
                return False
            p[find(i)] = find(r)
            vis[r] = True
            n -= 1
    return n == 1
"-----------------"
test()

