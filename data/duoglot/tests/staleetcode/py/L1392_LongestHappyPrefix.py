
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["level"]
    # output: "l"
    # EXPLANATION:  s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
    ,
    # example 2
    ["ababab"]
    # output: "abab"
    # EXPLANATION:  "abab" is the largest prefix which is also suffix. They can overlap in the original string.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestPrefix 
from typing import *
def f_gold(s: str) -> str:
    for i in range(1, len(s)):
        if s[:-i] == s[i:]:
            return s[i:]
    return ''
"-----------------"
test()

