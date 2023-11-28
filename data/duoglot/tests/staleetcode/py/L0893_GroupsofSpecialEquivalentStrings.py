
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]]
    # output: 3
    # EXPLANATION:   One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings is all pairwise special equivalent to these. The other two groups are ["xyzz", "zzxy"] and ["zzyx"]. Note that in particular, "zzxy" is not special equivalent to "zzyx".
    ,
    # example 2
    [["abc", "acb", "bac", "bca", "cab", "cba"]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numSpecialEquivGroups 
from typing import *
def f_gold(words: List[str]) -> int:
    s = {''.join(sorted(word[::2]) + sorted(word[1::2])) for word in words}
    return len(s)
"-----------------"
test()

