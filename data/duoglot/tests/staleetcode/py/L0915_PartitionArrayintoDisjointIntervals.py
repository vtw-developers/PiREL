
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 0, 3, 8, 6]]
    # output: 3
    # EXPLANATION:  left = [5,0,3], right = [8,6]
    ,
    # example 2
    [[1, 1, 1, 0, 6, 12]]
    # output: 4
    # EXPLANATION:  left = [1,1,1,0], right = [6,12]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### partitionDisjoint 
from typing import *
def f_gold(A):
    """
    :type A: List[int]
    :rtype: int
    """
    loc = 0
    vmx = A[0]
    mx = A[0]
    for i, el in enumerate(A):
        if el > mx:
            mx = el
        if el < vmx:
            loc = i
            vmx = mx
    return loc + 1
"-----------------"
test()

