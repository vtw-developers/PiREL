
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1], [2, 2]]
    # output: [1,2]
    ,
    # example 2
    [[1, 2], [2, 3]]
    # output: [1,2]
    ,
    # example 3
    [[2], [1, 3]]
    # output: [2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### fairCandySwap 
from typing import *
def f_gold(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    diff = (sum(aliceSizes) - sum(bobSizes)) >> 1
    s = set(bobSizes)
    for a in aliceSizes:
        target = a - diff
        if target in s:
            return [a, target]
"-----------------"
test()

