
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["{a,b}c{d,e}f"]
    # output: ["acdf","acef","bcdf","bcef"]
    ,
    # example 2
    ["abcd"]
    # output: ["abcd"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### expand 
from typing import *
def f_gold(s: str) -> List[str]:
    def convert(s):
        if not s:
            return
        if s[0] == '{':
            j = s.find('}')
            items.append(s[1:j].split(','))
            convert(s[j + 1 :])
        else:
            j = s.find('{')
            if j != -1:
                items.append(s[:j].split(','))
                convert(s[j:])
            else:
                items.append(s.split(','))
    def dfs(i, t):
        if i == len(items):
            ans.append(''.join(t))
            return
        for c in items[i]:
            t.append(c)
            dfs(i + 1, t)
            t.pop()
    items = []
    convert(s)
    ans = []
    dfs(0, [])
    ans.sort()
    return ans
"-----------------"
test()

