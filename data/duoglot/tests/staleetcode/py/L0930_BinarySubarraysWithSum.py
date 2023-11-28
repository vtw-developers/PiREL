
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 1, 0, 1], 2]
    # output: 4
    # EXPLANATION:  The 4 subarrays are bolded and underlined below:  [<u><strong>1,0,1</strong></u>,0,1]  [<u><strong>1,0,1,0</strong></u>,1]  [1,<u><strong>0,1,0,1</strong></u>]  [1,0,<u><strong>1,0,1</strong></u>]
    ,
    # example 2
    [[0, 0, 0, 0, 0], 0]
    # output: 15
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numSubarraysWithSum 
from typing import *
def f_gold(nums: List[int], goal: int) -> int:
    i1 = i2 = s1 = s2 = j = ans = 0
    n = len(nums)
    while j < n:
        s1 += nums[j]
        s2 += nums[j]
        while i1 <= j and s1 > goal:
            s1 -= nums[i1]
            i1 += 1
        while i2 <= j and s2 >= goal:
            s2 -= nums[i2]
            i2 += 1
        ans += i2 - i1
        j += 1
    return ans
"-----------------"
test()

