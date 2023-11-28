
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [3], [3], []]]
    # output: [[0,1,3],[0,2,3]]
    # EXPLANATION:  There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    ,
    # example 2
    [[[4, 3, 1], [3, 2, 4], [3], [4], []]]
    # output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### allPathsSourceTarget 
from collections import deque
from typing import *
def f_gold(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    q = deque([[0]])
    ans = []
    while q:
        path = q.popleft()
        u = path[-1]
        if u == n - 1:
            ans.append(path)
            continue
        for v in graph[u]:
            q.append(path + [v])
    return ans
"-----------------"
test()

