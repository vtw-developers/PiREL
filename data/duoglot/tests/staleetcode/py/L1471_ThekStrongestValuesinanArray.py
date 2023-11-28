
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5], 2]
    # output: [5,1]
    # EXPLANATION:  Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also <strong>accepted</strong> answer. Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.
    ,
    # example 2
    [[1, 1, 3, 5, 5], 2]
    # output: [5,5]
    # EXPLANATION:  Median is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].
    ,
    # example 3
    [[6, 7, 11, 7, 6, 8], 5]
    # output: [11,8,6,6,7]
    # EXPLANATION:  Median is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7]. Any permutation of [11,8,6,6,7] is <strong>accepted</strong>.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getStrongest 
from typing import *
def f_gold(arr: List[int], k: int) -> List[int]:
    arr.sort()
    m = arr[(len(arr) - 1) >> 1]
    arr.sort(key=lambda x: (-abs(x - m), -x))
    return arr[:k]
"-----------------"
test()

