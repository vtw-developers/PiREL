
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 3, 2, 2], 2, 2]
    # output: 11
    # EXPLANATION:  The elements at indices 0, 3, and 4 are divisible by p = 2. The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are: [2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2]. Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once. The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
    ,
    # example 2
    [[1, 2, 3, 4], 4, 1]
    # output: 10
    # EXPLANATION:  All element of nums are divisible by p = 1. Also, every subarray of nums will have at most 4 elements that are divisible by 1. Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countDistinct 
from typing import *
def f_gold(nums: List[int], k: int, p: int) -> int:
    n = len(nums)
    s = set()
    for i in range(n):
        cnt = 0
        t = ""
        for j in range(i, n):
            if nums[j] % p == 0:
                cnt += 1
            if cnt <= k:
                t += str(nums[j]) + ","
                s.add(t)
            else:
                break
    return len(s)
"-----------------"
test()

