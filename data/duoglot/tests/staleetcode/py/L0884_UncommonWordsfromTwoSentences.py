
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["this apple is sweet", "this apple is sour"]
    # output: ["sweet","sour"]
    ,
    # example 2
    ["apple apple", "banana"]
    # output: ["banana"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### uncommonFromSentences 
from collections import Counter
from typing import *
def f_gold(s1: str, s2: str) -> List[str]:
    c = Counter(s1.split()) + Counter(s2.split())
    return [w for w, n in c.items() if n == 1]
"-----------------"
test()

