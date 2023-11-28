
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abacbc"]
    # output: true
    # EXPLANATION:  The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
    ,
    # example 2
    ["aaabb"]
    # output: false
    # EXPLANATION:  The characters that appear in s are 'a' and 'b'. 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### areOccurrencesEqual 
from collections import Counter
from typing import *
def f_gold(s: str) -> bool:
    cnt = Counter(s)
    return len(set(cnt.values())) == 1
"-----------------"
test()

