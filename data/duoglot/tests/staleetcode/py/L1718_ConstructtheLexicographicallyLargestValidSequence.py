
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: [3,1,2,3,2]
    # EXPLANATION:  [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
    ,
    # example 2
    [5]
    # output: [5,3,1,4,3,5,2,4,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### constructDistancedSequence 
from typing import *
def f_gold(n: int) -> List[int]:
    def dfs(u):
        if u == n * 2:
            return True
        if path[u]:
            return dfs(u + 1)
        for i in range(n, 1, -1):
            if cnt[i] and u + i < n * 2 and path[u + i] == 0:
                cnt[i] = 0
                path[u] = path[u + i] = i
                if dfs(u + 1):
                    return True
                path[u] = path[u + i] = 0
                cnt[i] = 2
        if cnt[1]:
            cnt[1], path[u] = 0, 1
            if dfs(u + 1):
                return True
            path[u], cnt[1] = 0, 1
        return False
    path = [0] * (n * 2)
    cnt = [2] * (n * 2)
    cnt[1] = 1
    dfs(1)
    return path[1:]
"-----------------"
test()

