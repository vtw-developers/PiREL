
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aab"]
    # output: "aba"
    ,
    # example 2
    ["aaab"]
    # output: ""
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reorganizeString 
from collections import Counter
from typing import *
def f_gold(s: str) -> str:
    n = len(s)
    cnt = Counter(s)
    mx = max(cnt.values())
    if mx > (n + 1) // 2:
        return ''
    i = 0
    ans = [None] * n
    for k, v in cnt.most_common():
        while v:
            ans[i] = k
            v -= 1
            i += 2
            if i >= n:
                i = 1
    return ''.join(ans)
"-----------------"
test()

