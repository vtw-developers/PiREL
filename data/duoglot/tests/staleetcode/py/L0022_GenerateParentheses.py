
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: ["((()))","(()())","(())()","()(())","()()()"]
    ,
    # example 2
    [1]
    # output: ["()"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### generateParenthesis 
from typing import *
def f_gold(n: int) -> List[str]:
    def dfs(left, right, t):
        if left == n and right == n:
            ans.append(t)
            return
        if left < n:
            dfs(left + 1, right, t + '(')
        if right < left:
            dfs(left, right + 1, t + ')')
    ans = []
    dfs(0, 0, '')
    return ans
"-----------------"
test()

