
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["pay", "attention", "practice", "attend"], "at"]
    # output: 2
    # EXPLANATION:  The 2 strings that contain "at" as a prefix are: "<u><strong>at</strong></u>tention" and "<u><strong>at</strong></u>tend".
    ,
    # example 2
    [["leetcode", "win", "loops", "success"], "code"]
    # output: 0
    # EXPLANATION:  There are no strings that contain "code" as a prefix.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### prefixCount 
from typing import *
def f_gold(words: List[str], pref: str) -> int:
    return sum(w.startswith(pref) for w in words)
"-----------------"
test()

