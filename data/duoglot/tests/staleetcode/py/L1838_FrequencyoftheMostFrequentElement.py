
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 4], 5]
    # output: 3<strong>
    # EXPLANATION: </strong> Increment the first element three times and the second element two times to make nums = [4,4,4]. 4 has a frequency of 3.
    ,
    # example 2
    [[1, 4, 8, 13], 5]
    # output: 2
    # EXPLANATION:  There are multiple optimal solutions: - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2. - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2. - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
    ,
    # example 3
    [[3, 9, 6], 2]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxFrequency 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    nums.sort()
    ans = 1
    window = 0
    l, r, n = 0, 1, len(nums)
    while r < n:
        window += (nums[r] - nums[r - 1]) * (r - l)
        r += 1
        while window > k:
            window -= nums[r - 1] - nums[l]
            l += 1
        ans = max(ans, r - l)
    return ans
"-----------------"
test()

