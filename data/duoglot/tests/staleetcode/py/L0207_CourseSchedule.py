
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [[1, 0]]]
    # output: true
    # EXPLANATION:  There are a total of 2 courses to take.  To take course 1 you should have finished course 0. So it is possible.
    ,
    # example 2
    [2, [[1, 0], [0, 1]]]
    # output: false
    # EXPLANATION:  There are a total of 2 courses to take.  To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canFinish 
from collections import deque
from collections import defaultdict
from typing import *
def f_gold(numCourses: int, prerequisites: List[List[int]]) -> bool:
    edges = defaultdict(list)
    indegree = [0] * numCourses
    for a, b in prerequisites:
        edges[b].append(a)
        indegree[a] += 1
    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)
    n = 0
    while q:
        b = q.popleft()
        n += 1
        for a in edges[b]:
            indegree[a] -= 1
            if indegree[a] == 0:
                q.append(a)
    return n == numCourses
"-----------------"
test()

