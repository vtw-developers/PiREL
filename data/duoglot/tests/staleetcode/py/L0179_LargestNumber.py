
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 2]]
    # output: "210"
    ,
    # example 2
    [[3, 30, 34, 5, 9]]
    # output: "9534330"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
from functools import cmp_to_key
### largestNumber 
from typing import *
def f_gold(nums: List[int]) -> str:
    num_list = list(map(str, nums))
    num_list.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
    return '0' if num_list[0] == '0' else ''.join(num_list)
"-----------------"
test()

