
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 5, 1]]
    # output: true
    # EXPLANATION: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
    ,
    # example 2
    [[1, 2, 4]]
    # output: false
    # EXPLANATION: There is no way to reorder the elements to obtain an arithmetic progression.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canMakeArithmeticProgression 
from typing import *
def f_gold(arr: List[int]) -> bool:
    arr.sort()
    for i in range(1, len(arr) - 1):
        if (arr[i] << 1) != arr[i - 1] + arr[i + 1]:
            return False
    return True
"-----------------"
test()

