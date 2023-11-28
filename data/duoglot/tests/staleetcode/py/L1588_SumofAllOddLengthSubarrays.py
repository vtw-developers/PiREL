
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 4, 2, 5, 3]]
    # output: 58
    # EXPLANATION: The odd-length subarrays of arr and their sums are: [1] = 1 [4] = 4 [2] = 2 [5] = 5 [3] = 3 [1,4,2] = 7 [4,2,5] = 11 [2,5,3] = 10 [1,4,2,5,3] = 15 If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
    ,
    # example 2
    [[1, 2]]
    # output: 3
    # EXPLANATION: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
    ,
    # example 3
    [[10, 11, 12]]
    # output: 66
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumOddLengthSubarrays 
from typing import *
def f_gold(arr: List[int]) -> int:
    n = len(arr)
    presum = [0] * (n + 1)
    for i in range(n):
        presum[i + 1] = presum[i] + arr[i]
    res = 0
    for i in range(n):
        for j in range(0, n, 2):
            if i + j < n:
                res += presum[i + j + 1] - presum[i]
    return res
"-----------------"
test()

