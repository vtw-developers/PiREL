
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]]
    # output: 5
    ,
    # example 2
    [[[1, 2, 3], [2, 3, 4], [2, 3, 5]]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### smallestCommonElement 
from collections import Counter
from typing import *
def f_gold(mat: List[List[int]]) -> int:
    counter = Counter()
    for row in mat:
        for num in row:
            counter[num] += 1
            if counter[num] == len(mat):
                return num
    return -1
"-----------------"
test()

