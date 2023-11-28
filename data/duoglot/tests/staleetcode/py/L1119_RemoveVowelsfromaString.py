
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leetcodeisacommunityforcoders"]
    # output: "ltcdscmmntyfrcdrs"
    ,
    # example 2
    ["aeiou"]
    # output: ""
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### removeVowels 
from typing import *
def f_gold(s: str) -> str:
    res = []
    for c in s:
        if c not in {'a', 'e', 'i', 'o', 'u'}:
            res.append(c)
    return ''.join(res)
"-----------------"
test()

