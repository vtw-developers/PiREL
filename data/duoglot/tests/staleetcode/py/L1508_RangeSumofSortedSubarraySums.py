
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], 4, 1, 5]
    # output: 13
    # EXPLANATION:  All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.
    ,
    # example 2
    [[1, 2, 3, 4], 4, 3, 4]
    # output: 6
    # EXPLANATION:  The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
    ,
    # example 3
    [[1, 2, 3, 4], 4, 1, 10]
    # output: 50
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rangeSum 
from typing import *
def f_gold(nums: List[int], n: int, left: int, right: int) -> int:
    arr = []
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            arr.append(s)
    arr.sort()
    MOD = 10**9 + 7
    return sum(arr[left - 1 : right]) % MOD
"-----------------"
test()

