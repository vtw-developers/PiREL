
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["codeleet", [4, 5, 6, 7, 0, 2, 1, 3]]
    # output: "leetcode"
    # EXPLANATION:  As shown, "codeleet" becomes "leetcode" after shuffling.
    ,
    # example 2
    ["abc", [0, 1, 2]]
    # output: "abc"
    # EXPLANATION:  After shuffling, each character remains in its position.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### restoreString 
from typing import *
def f_gold(s: str, indices: List[int]) -> str:
    ans = [0] * len(s)
    for i, c in enumerate(s):
        ans[indices[i]] = c
    return ''.join(ans)
"-----------------"
test()

