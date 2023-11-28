
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leetcode"]
    # output: 2
    # EXPLANATION:  The substring "ee" is of length 2 with the character 'e' only.
    ,
    # example 2
    ["abbcccddddeeeeedcba"]
    # output: 5
    # EXPLANATION:  The substring "eeeee" is of length 5 with the character 'e' only.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxPower 
from typing import *
def f_gold(s: str) -> int:
    ans = t = 0
    for i, c in enumerate(s):
        if i == 0 or c == s[i - 1]:
            t += 1
        else:
            t = 1
        ans = max(ans, t)
    return ans
"-----------------"
test()

