
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["eceba"]
    # output: 3
    # EXPLANATION:  The substring is "ece" which its length is 3.
    ,
    # example 2
    ["ccaabbb"]
    # output: 5
    # EXPLANATION:  The substring is "aabbb" which its length is 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lengthOfLongestSubstringTwoDistinct 
from collections import Counter
from typing import *
def f_gold(s: str) -> int:
    mp = Counter()
    i = j = ans = 0
    for c in s:
        mp[c] += 1
        while len(mp) > 2:
            mp[s[i]] -= 1
            if mp[s[i]] == 0:
                mp.pop(s[i])
            i += 1
        ans = max(ans, j - i + 1)
        j += 1
    return ans
"-----------------"
test()

