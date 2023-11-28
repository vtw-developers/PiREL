
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 4, 1, 1, 6, 5]]
    # output: 3
    # EXPLANATION:  At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley. At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill.  At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley. At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2. At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill. At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley.  There are 3 hills and valleys so we return 3.
    ,
    # example 2
    [[6, 6, 5, 5, 4, 1]]
    # output: 0
    # EXPLANATION:  At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley. At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley. At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley. At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley. At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley. At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley. There are 0 hills and valleys so we return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countHillValley 
from typing import *
def f_gold(nums: List[int]) -> int:
    ans = j = 0
    for i in range(1, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            continue
        if nums[i] > nums[j] and nums[i] > nums[i + 1]:
            ans += 1
        if nums[i] < nums[j] and nums[i] < nums[i + 1]:
            ans += 1
        j = i
    return ans
"-----------------"
test()

