
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["a", "b"]
    # output: false
    ,
    # example 2
    ["aa", "ab"]
    # output: false
    ,
    # example 3
    ["aa", "aab"]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canConstruct 
from collections import Counter
from typing import *
def f_gold(ransomNote: str, magazine: str) -> bool:
    counter = Counter(magazine)
    for c in ransomNote:
        if counter[c] <= 0:
            return False
        counter[c] -= 1
    return True
"-----------------"
test()

