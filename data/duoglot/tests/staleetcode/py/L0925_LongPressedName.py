
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["alex", "aaleex"]
    # output: true
    # EXPLANATION: 'a' and 'e' in 'alex' were long pressed.
    ,
    # example 2
    ["saeed", "ssaaedd"]
    # output: false
    # EXPLANATION: 'e' must have been pressed twice, but it was not in the typed output.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isLongPressedName 
from typing import *
def f_gold(name: str, typed: str) -> bool:
    m, n = len(name), len(typed)
    i = j = 0
    while i < m and j < n:
        if name[i] != typed[j]:
            return False
        cnt1 = cnt2 = 0
        c = name[i]
        while i + 1 < m and name[i + 1] == c:
            i += 1
            cnt1 += 1
        while j + 1 < n and typed[j + 1] == c:
            j += 1
            cnt2 += 1
        if cnt1 > cnt2:
            return False
        i, j = i + 1, j + 1
    return i == m and j == n
"-----------------"
test()

