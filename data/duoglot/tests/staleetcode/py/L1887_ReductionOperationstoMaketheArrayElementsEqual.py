
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 1, 3]]
    # output: 3
    # EXPLANATION:  It takes 3 operations to make all elements in nums equal: 1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [<u>3</u>,1,3]. 2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [<u>1</u>,1,3]. 3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,<u>1</u>].
    ,
    # example 2
    [[1, 1, 1]]
    # output: 0
    # EXPLANATION:  All elements in nums are already equal.
    ,
    # example 3
    [[1, 1, 2, 2, 3]]
    # output: 4
    # EXPLANATION:  It takes 4 operations to make all elements in nums equal: 1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2,<u>2</u>]. 2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,<u>1</u>,2,2]. 3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1,<u>1</u>,2]. 4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1,<u>1</u>].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reductionOperations 
from typing import *
def f_gold(nums: List[int]) -> int:
    nums.sort()
    cnt, res, n = 0, 0, len(nums)
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            cnt += 1
        res += cnt
    return res
"-----------------"
test()

