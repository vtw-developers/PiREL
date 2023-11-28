
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 2, 2]]
    # output: true
    # EXPLANATION:  You can form a square with length 2, one side of the square came two sticks with length 1.
    ,
    # example 2
    [[3, 3, 3, 3, 4]]
    # output: false
    # EXPLANATION:  You cannot find a way to form a square with all the matchsticks.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### makesquare 
from typing import *
def f_gold(matchsticks: List[int]) -> bool:
    def dfs(u):
        if u == len(matchsticks):
            return True
        for i in range(4):
            if i > 0 and edges[i - 1] == edges[i]:
                continue
            edges[i] += matchsticks[u]
            if edges[i] <= x and dfs(u + 1):
                return True
            edges[i] -= matchsticks[u]
        return False
    x, mod = divmod(sum(matchsticks), 4)
    if mod or x < max(matchsticks):
        return False
    edges = [0] * 4
    matchsticks.sort(reverse=True)
    return dfs(0)
"-----------------"
test()

