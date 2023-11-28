
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 5, 8], [10, 9, 1, 8], 2]
    # output: 2
    # EXPLANATION:   For arr1[0]=4 we have:  |4-10|=6 > d=2  |4-9|=5 > d=2  |4-1|=3 > d=2  |4-8|=4 > d=2  For arr1[1]=5 we have:  |5-10|=5 > d=2  |5-9|=4 > d=2  |5-1|=4 > d=2  |5-8|=3 > d=2 For arr1[2]=8 we have: <strong>|8-10|=2 <= d=2</strong> <strong>|8-9|=1 <= d=2</strong> |8-1|=7 > d=2 <strong>|8-8|=0 <= d=2</strong>
    ,
    # example 2
    [[1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3]
    # output: 2
    ,
    # example 3
    [[2, 1, 100, 3], [-5, -2, 10, -3, 7], 6]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findTheDistanceValue 
from typing import *
def f_gold(arr1: List[int], arr2: List[int], d: int) -> int:
    return sum(all(abs(a - b) > d for b in arr2) for a in arr1)
"-----------------"
test()

