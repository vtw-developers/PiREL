
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2, 1, 1, 3]]
    # output: true
    # EXPLANATION:  The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
    ,
    # example 2
    [[1, 2]]
    # output: false
    ,
    # example 3
    [[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### uniqueOccurrences 
from collections import Counter
from typing import *
def f_gold(arr: List[int]) -> bool:
    counter = Counter(arr)
    s = set()
    for num in counter.values():
        if num in s:
            return False
        s.add(num)
    return True
"-----------------"
test()

