
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["bank", "kanb"]
    # output: true
    # EXPLANATION:  For example, swap the first character with the last character of s2 to make "bank".
    ,
    # example 2
    ["attack", "defend"]
    # output: false
    # EXPLANATION:  It is impossible to make them equal with one string swap.
    ,
    # example 3
    ["kelb", "kelb"]
    # output: true
    # EXPLANATION:  The two strings are already equal, so no string swap operation is required.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### areAlmostEqual 
from typing import *
def f_gold(s1: str, s2: str) -> bool:
    cnt, n = 0, len(s1)
    c1 = c2 = None
    for i in range(n):
        if s1[i] != s2[i]:
            cnt += 1
            if (cnt == 2 and (s1[i] != c2 or s2[i] != c1)) or cnt > 2:
                return False
            c1, c2 = s1[i], s2[i]
    return cnt == 0 or cnt == 2
"-----------------"
test()

