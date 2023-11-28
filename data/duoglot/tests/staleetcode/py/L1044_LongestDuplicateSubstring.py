
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["banana"]
    # output: "ana"
    ,
    # example 2
    ["abcd"]
    # output: ""
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestDupSubstring 
from typing import *
def f_gold(s: str) -> str:
    def check(l):
        vis = set()
        for i in range(n - l + 1):
            t = s[i : i + l]
            if t in vis:
                return t
            vis.add(t)
        return ''
    n = len(s)
    left, right = 0, n
    ans = ''
    while left < right:
        mid = (left + right + 1) >> 1
        t = check(mid)
        ans = t or ans
        if t:
            left = mid
        else:
            right = mid - 1
    return ans
"-----------------"
test()

