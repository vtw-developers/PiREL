
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["12"]
    # output: 2
    # EXPLANATION:  "12" could be decoded as "AB" (1 2) or "L" (12).
    ,
    # example 2
    ["226"]
    # output: 3
    # EXPLANATION:  "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
    ,
    # example 3
    ["06"]
    # output: 0
    # EXPLANATION:  "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numDecodings 
from typing import *
def f_gold(s: str) -> int:
    n = len(s)
    a, b, c = 0, 1, 0
    for i in range(1, n + 1):
        c = 0
        if s[i - 1] != '0':
            c += b
        if i > 1 and s[i - 2] != '0' and (int(s[i - 2]) * 10 + int(s[i - 1]) <= 26):
            c += a
        a, b = b, c
    return c
"-----------------"
test()

