
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 5, 0, -2, -3, 1], 5]
    # output: 7
    # EXPLANATION:  There are 7 subarrays with a sum divisible by k = 5: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
    ,
    # example 2
    [[5], 9]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### subarraysDivByK 
from collections import Counter
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    ans = s = 0
    counter = Counter({0: 1})
    for num in nums:
        s += num
        ans += counter[s % k]
        counter[s % k] += 1
    return ans
"-----------------"
test()

