
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-4, -2, 2, 4], 1, 3, 5]
    # output: [3,9,15,33]
    ,
    # example 2
    [[-4, -2, 2, 4], -1, 3, 5]
    # output: [-23,-5,1,7]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortTransformedArray 
from typing import *
def f_gold(nums: List[int], a: int, b: int, c: int
) -> List[int]:
    def f(x):
        return a * x * x + b * x + c
    n = len(nums)
    i, j, k = 0, n - 1, 0 if a < 0 else n - 1
    res = [0] * n
    while i <= j:
        v1, v2 = f(nums[i]), f(nums[j])
        if a < 0:
            if v1 <= v2:
                res[k] = v1
                i += 1
            else:
                res[k] = v2
                j -= 1
            k += 1
        else:
            if v1 >= v2:
                res[k] = v1
                i += 1
            else:
                res[k] = v2
                j -= 1
            k -= 1
    return res
"-----------------"
test()

