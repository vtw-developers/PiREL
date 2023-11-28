
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: ["11","69","88","96"]
    ,
    # example 2
    [1]
    # output: ["0","1","8"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findStrobogrammatic 
from typing import *
def f_gold(n: int) -> List[str]:
    def dfs(u):
        if u == 0:
            return ['']
        if u == 1:
            return ['0', '1', '8']
        ans = []
        for v in dfs(u - 2):
            for l, r in [['1', '1'], ['8', '8'], ['6', '9'], ['9', '6']]:
                ans.append(l + v + r)
            if u != n:
                ans.append('0' + v + '0')
        return ans
    return dfs(n)
"-----------------"
test()

