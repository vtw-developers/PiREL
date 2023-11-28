
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]]
    # output: [2,2,2,1,4,3,3,9,6,7,19]
    ,
    # example 2
    [[28, 6, 22, 8, 44, 17], [22, 28, 8, 6]]
    # output: [22,28,8,6,17,44]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### relativeSortArray 
from typing import *
def f_gold(arr1: List[int], arr2: List[int]) -> List[int]:
    mp = [0] * 1001
    for x in arr1:
        mp[x] += 1
    i = 0
    for x in arr2:
        while mp[x] > 0:
            arr1[i] = x
            mp[x] -= 1
            i += 1
    for x, cnt in enumerate(mp):
        for _ in range(cnt):
            arr1[i] = x
            i += 1
    return arr1
"-----------------"
test()

