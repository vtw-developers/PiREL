
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [[1, 0], [1, 2], [1, 3]]]
    # output: [1]
    # EXPLANATION:  As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
    ,
    # example 2
    [6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]]
    # output: [3,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMinHeightTrees 
from collections import deque
from collections import defaultdict
from typing import *
def f_gold(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    g = defaultdict(list)
    degree = [0] * n
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
        degree[a] += 1
        degree[b] += 1
    q = deque()
    for i in range(n):
        if degree[i] == 1:
            q.append(i)
    ans = []
    while q:
        n = len(q)
        ans.clear()
        for _ in range(n):
            a = q.popleft()
            ans.append(a)
            for b in g[a]:
                degree[b] -= 1
                if degree[b] == 1:
                    q.append(b)
    return ans
"-----------------"
test()

