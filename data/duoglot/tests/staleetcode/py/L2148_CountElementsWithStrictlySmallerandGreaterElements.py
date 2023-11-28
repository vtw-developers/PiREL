
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[11, 7, 2, 15]]
    # output: 2
    # EXPLANATION:  The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it. Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it. In total there are 2 elements having both a strictly smaller and a strictly greater element appear in <code>nums</code>.
    ,
    # example 2
    [[-3, 3, 3, 90]]
    # output: 2
    # EXPLANATION:  The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it. Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in <code>nums</code>.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countElements 
from typing import *
def f_gold(nums: List[int]) -> int:
    mi, mx = min(nums), max(nums)
    return sum(mi < num < mx for num in nums)
"-----------------"
test()

