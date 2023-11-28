
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 7, 3, 9, 4, 9, 8, 3, 1]]
    # output: 8
    # EXPLANATION:  The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
    ,
    # example 2
    [[9, 9, 8, 8]]
    # output: -1
    # EXPLANATION:  There is no number that occurs only once.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestUniqueNumber 
from collections import Counter
from typing import *
def f_gold(A: List[int]) -> int:
    counter = Counter(A)
    for i in range(1000, -1, -1):
        if counter[i] == 1:
            return i
    return -1
"-----------------"
test()

