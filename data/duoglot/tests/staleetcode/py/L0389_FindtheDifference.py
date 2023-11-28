
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcd", "abcde"]
    # output: "e"
    # EXPLANATION:  'e' is the letter that was added.
    ,
    # example 2
    ["", "y"]
    # output: "y"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findTheDifference 
from collections import Counter
from typing import *
def f_gold(s: str, t: str) -> str:
    counter = Counter(s)
    for c in t:
        if counter[c] <= 0:
            return c
        counter[c] -= 1
    return None
"-----------------"
test()

