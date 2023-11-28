
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 2]]
    # output: 4
    # EXPLANATION:  The unique elements are [1,3], and the sum is 4.
    ,
    # example 2
    [[1, 1, 1, 1, 1]]
    # output: 0
    # EXPLANATION:  There are no unique elements, and the sum is 0.
    ,
    # example 3
    [[1, 2, 3, 4, 5]]
    # output: 15
    # EXPLANATION:  The unique elements are [1,2,3,4,5], and the sum is 15.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumOfUnique 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> int:
    counter = Counter(nums)
    return sum(num for num, cnt in counter.items() if cnt == 1)
"-----------------"
test()

