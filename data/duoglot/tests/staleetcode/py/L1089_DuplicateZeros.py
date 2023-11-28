
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 2, 3, 0, 4, 5, 0]]
    # output: [1,0,0,2,3,0,0,4]
    # EXPLANATION:  After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
    ,
    # example 2
    [[1, 2, 3]]
    # output: [1,2,3]
    # EXPLANATION:  After calling your function, the input array is modified to: [1,2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### duplicateZeros 
from typing import *
def f_gold(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    i, k = -1, 0
    while k < n:
        i += 1
        k += 1 if arr[i] else 2
    j = n - 1
    if k == n + 1:
        arr[j] = 0
        i, j = i - 1, j - 1
    while ~j:
        if arr[i] == 0:
            arr[j] = arr[j - 1] = arr[i]
            j -= 1
        else:
            arr[j] = arr[i]
        i, j = i - 1, j - 1
"-----------------"
test()

