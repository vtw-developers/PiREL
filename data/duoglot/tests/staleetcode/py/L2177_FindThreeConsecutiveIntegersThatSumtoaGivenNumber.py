
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [33]
    # output: [10,11,12]
    # EXPLANATION:  33 can be expressed as 10 + 11 + 12 = 33. 10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
    ,
    # example 2
    [4]
    # output: []
    # EXPLANATION:  There is no way to express 4 as the sum of 3 consecutive integers.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumOfThree 
from typing import *
def f_gold(num: int) -> List[int]:
    a, b = divmod(num, 3)
    return [] if b else [a - 1, a, a + 1]
"-----------------"
test()

