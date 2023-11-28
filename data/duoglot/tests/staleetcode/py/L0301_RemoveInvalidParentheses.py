
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["()())()"]
    # output: ["(())()","()()()"]
    ,
    # example 2
    ["(a)())()"]
    # output: ["(a())()","(a)()()"]
    ,
    # example 3
    [")("]
    # output: [""]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### removeInvalidParentheses 
from typing import *
def f_gold(s: str) -> List[str]:
    def dfs(i, t, lcnt, rcnt, ldel, rdel):
        nonlocal tdel, ans
        if ldel * rdel < 0 or lcnt < rcnt or ldel + rdel > len(s) - i:
            return
        if ldel == 0 and rdel == 0:
            if len(s) - len(t) == tdel:
                ans.add(t)
        if i == len(s):
            return
        if s[i] == '(':
            dfs(i + 1, t, lcnt, rcnt, ldel - 1, rdel)
            dfs(i + 1, t + '(', lcnt + 1, rcnt, ldel, rdel)
        elif s[i] == ')':
            dfs(i + 1, t, lcnt, rcnt, ldel, rdel - 1)
            dfs(i + 1, t + ')', lcnt, rcnt + 1, ldel, rdel)
        else:
            dfs(i + 1, t + s[i], lcnt, rcnt, ldel, rdel)
    ldel = rdel = 0
    for c in s:
        if c == '(':
            ldel += 1
        elif c == ')':
            if ldel == 0:
                rdel += 1
            else:
                ldel -= 1
    tdel = ldel + rdel
    ans = set()
    dfs(0, '', 0, 0, ldel, rdel)
    return list(ans)
"-----------------"
test()

