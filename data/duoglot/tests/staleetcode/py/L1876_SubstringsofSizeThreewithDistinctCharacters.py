
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["xyzzaz"]
    # output: 1
    # EXPLANATION:  There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".  The only good substring of length 3 is "xyz".
    ,
    # example 2
    ["aababcabc"]
    # output: 4
    # EXPLANATION:  There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc". The good substrings are "abc", "bca", "cab", and "abc".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countGoodSubstrings 
from typing import *
def f_gold(s: str) -> int:
    count, n = 0, len(s)
    for i in range(n - 2):
        count += s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]
    return count
"-----------------"
test()

