
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcd", "cdabcdab"]
    # output: 3
    # EXPLANATION:  We return 3 because by repeating a three times "ab<strong>cdabcdab</strong>cd", b is a substring of it.
    ,
    # example 2
    ["a", "aa"]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### repeatedStringMatch 
import math
from math import ceil
from typing import *
def f_gold(a: str, b: str) -> int:
    m, n = len(a), len(b)
    ans = ceil(n / m)
    t = [a] * ans
    for _ in range(3):
        if b in ''.join(t):
            return ans
        ans += 1
        t.append(a)
    return -1
"-----------------"
test()

