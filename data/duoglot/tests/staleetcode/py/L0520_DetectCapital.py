
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["USA"]
    # output: true
    ,
    # example 2
    ["FlaG"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### detectCapitalUse 
from typing import *
def f_gold(word: str) -> bool:
    cnt = 0
    for c in word:
        if c.isupper():
            cnt += 1
    return cnt == 0 or cnt == len(word) or (cnt == 1 and word[0].isupper())
"-----------------"
test()

