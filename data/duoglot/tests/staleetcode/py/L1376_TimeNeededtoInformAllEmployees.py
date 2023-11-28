
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 0, [-1], [0]]
    # output: 0
    # EXPLANATION:  The head of the company is the only employee in the company.
    ,
    # example 2
    [6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]]
    # output: 1
    # EXPLANATION:  The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all. The tree structure of the employees in the company is shown.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numOfMinutes 
import math
from math import inf
from collections import defaultdict
from typing import *
def f_gold(n: int, headID: int, manager: List[int], informTime: List[int]
) -> int:
    def dfs(i):
        ans = 0
        for j in g[i]:
            ans = max(ans, informTime[i] + dfs(j))
        return ans
    g = defaultdict(list)
    for i, m in enumerate(manager):
        g[m].append(i)
    return dfs(headID)
"-----------------"
test()

