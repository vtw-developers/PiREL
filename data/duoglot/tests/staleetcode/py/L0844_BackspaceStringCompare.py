
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab#c", "ad#c"]
    # output: true
    # EXPLANATION:  Both s and t become "ac".
    ,
    # example 2
    ["ab##", "c#d#"]
    # output: true
    # EXPLANATION:  Both s and t become "".
    ,
    # example 3
    ["a#c", "b"]
    # output: false
    # EXPLANATION:  s becomes "c" while t becomes "b".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### backspaceCompare 
from typing import *
def f_gold(s: str, t: str) -> bool:
    i, j, skip1, skip2 = len(s) - 1, len(t) - 1, 0, 0
    while i >= 0 or j >= 0:
        while i >= 0:
            if s[i] == '#':
                skip1 += 1
                i -= 1
            elif skip1:
                skip1 -= 1
                i -= 1
            else:
                break
        while j >= 0:
            if t[j] == '#':
                skip2 += 1
                j -= 1
            elif skip2:
                skip2 -= 1
                j -= 1
            else:
                break
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False
        i, j = i - 1, j - 1
    return True
"-----------------"
test()

