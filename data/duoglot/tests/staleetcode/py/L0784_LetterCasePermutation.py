
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["a1b2"]
    # output: ["a1b2","a1B2","A1b2","A1B2"]
    ,
    # example 2
    ["3z4"]
    # output: ["3z4","3Z4"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### letterCasePermutation 
from typing import *
def f_gold(s: str) -> List[str]:
    def dfs(i, t):
        if i == len(t):
            ans.append(''.join(t))
            return
        dfs(i + 1, t)
        if t[i].isalpha():
            t[i] = t[i].upper() if t[i].islower() else t[i].lower()
            dfs(i + 1, t)
    ans = []
    t = list(s)
    dfs(0, t)
    return ans
"-----------------"
test()

