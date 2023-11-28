
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abc", "ahbgdc"]
    # output: true
    ,
    # example 2
    ["axc", "ahbgdc"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isSubsequence 
from typing import *
def f_gold(s: str, t: str) -> bool:
    i, j, m, n = 0, 0, len(s), len(t)
    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == m
"-----------------"
test()

