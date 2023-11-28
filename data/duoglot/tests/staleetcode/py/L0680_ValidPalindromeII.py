
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aba"]
    # output: true
    ,
    # example 2
    ["abca"]
    # output: true
    # EXPLANATION:  You could delete the character 'c'.
    ,
    # example 3
    ["abc"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### validPalindrome 
from typing import *
def f_gold(s: str) -> bool:
    def check(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return check(i, j - 1) or check(i + 1, j)
        i, j = i + 1, j - 1
    return True
"-----------------"
test()

