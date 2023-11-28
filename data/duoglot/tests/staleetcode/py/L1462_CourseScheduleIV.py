
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [[1, 0]], [[0, 1], [1, 0]]]
    # output: [false,true]
    # EXPLANATION:  The pair [1, 0] indicates that you have to take course 1 before you can take course 0. Course 0 is not a prerequisite of course 1, but the opposite is true.
    ,
    # example 2
    [2, [], [[1, 0], [0, 1]]]
    # output: [false,false]
    # EXPLANATION:  There are no prerequisites, and each course is independent.
    ,
    # example 3
    [3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]]
    # output: [true,true]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkIfPrerequisite 
def cache(f): return f
from collections import defaultdict
from typing import *
def f_gold(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    @cache
    def dfs(a, b):
        if b in g[a] or a == b:
            return True
        for c in g[a]:
            if dfs(c, b):
                return True
        return False
    g = defaultdict(set)
    for a, b in prerequisites:
        g[a].add(b)
    return [dfs(a, b) for a, b in queries]
"-----------------"
test()

