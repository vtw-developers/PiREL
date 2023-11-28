
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 0, 1, 1, 0, 0]]
    # output: 1
    # EXPLANATION:  Here are a few of the ways to group all the 1's together: [0,<u>0</u>,<u>1</u>,1,1,0,0] using 1 swap. [0,1,<u>1</u>,1,<u>0</u>,0,0] using 1 swap. [1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array). There is no way to group all 1's together with 0 swaps. Thus, the minimum number of swaps required is 1.
    ,
    # example 2
    [[0, 1, 1, 1, 0, 0, 1, 1, 0]]
    # output: 2
    # EXPLANATION:  Here are a few of the ways to group all the 1's together: [1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array). [1,1,1,1,1,0,0,0,0] using 2 swaps. There is no way to group all 1's together with 0 or 1 swaps. Thus, the minimum number of swaps required is 2.
    ,
    # example 3
    [[1, 1, 0, 0, 1]]
    # output: 0
    # EXPLANATION:  All the 1's are already grouped together due to the circular property of the array. Thus, the minimum number of swaps required is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSwaps 
from typing import *
def f_gold(nums: List[int]) -> int:
    cnt = nums.count(1)
    n = len(nums)
    s = [0] * ((n << 1) + 1)
    for i in range(n << 1):
        s[i + 1] = s[i] + nums[i % n]
    mx = 0
    for i in range(n << 1):
        j = i + cnt - 1
        if j < (n << 1):
            mx = max(mx, s[j + 1] - s[i])
    return cnt - mx
"-----------------"
test()

