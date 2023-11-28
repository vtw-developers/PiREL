
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["word"]
    # output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
    ,
    # example 2
    ["a"]
    # output: ["1","a"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### generateAbbreviations 
from typing import *
def f_gold(word: str) -> List[str]:
    def dfs(s, t):
        if not s:
            ans.append(''.join(t))
            return
        for i in range(1, len(s) + 1):
            t.append(str(i))
            if i < len(s):
                t.append(s[i])
                dfs(s[i + 1 :], t)
                t.pop()
            else:
                dfs(s[i:], t)
            t.pop()
        t.append(s[0])
        dfs(s[1:], t)
        t.pop()
    ans = []
    dfs(word, [])
    return ans
"-----------------"
test()

