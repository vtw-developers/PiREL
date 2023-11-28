
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aacecaaa"]
    # output: "aaacecaaa"
    ,
    # example 2
    ["abcd"]
    # output: "dcbabcd"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestPalindrome 
from typing import *
def f_gold(s: str) -> str:
    base = 131
    mod = 10**9 + 7
    n = len(s)
    prefix = suffix = 0
    mul = 1
    idx = 0
    for i, c in enumerate(s):
        prefix = (prefix * base + (ord(c) - ord('a') + 1)) % mod
        suffix = (suffix + (ord(c) - ord('a') + 1) * mul) % mod
        mul = (mul * base) % mod
        if prefix == suffix:
            idx = i + 1
    return s if idx == n else s[idx:][::-1] + s
"-----------------"
test()

