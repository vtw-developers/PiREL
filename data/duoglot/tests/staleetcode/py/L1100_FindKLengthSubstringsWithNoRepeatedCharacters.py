
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["havefunonleetcode", 5]
    # output: 6
    # EXPLANATION:  There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
    ,
    # example 2
    ["home", 5]
    # output: 0
    # EXPLANATION:  Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numKLenSubstrNoRepeats 
from typing import *
def f_gold(s: str, k: int) -> int:
    ans = j = 0
    mp = {}
    for i, c in enumerate(s):
        if c in mp:
            j = max(j, mp[c] + 1)
        mp[c] = i
        if i - j + 1 >= k:
            ans += 1
    return ans
"-----------------"
test()

