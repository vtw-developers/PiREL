
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 1, 2, 3]]
    # output: [2,3,4,1]
    # EXPLANATION:   First, we sort the values present at odd indices (1 and 3) in non-increasing order. So, nums changes from [4,<strong><u>1</u></strong>,2,<strong><u>3</u></strong>] to [4,<u><strong>3</strong></u>,2,<strong><u>1</u></strong>]. Next, we sort the values present at even indices (0 and 2) in non-decreasing order. So, nums changes from [<u><strong>4</strong></u>,1,<strong><u>2</u></strong>,3] to [<u><strong>2</strong></u>,3,<u><strong>4</strong></u>,1]. Thus, the array formed after rearranging the values is [2,3,4,1].
    ,
    # example 2
    [[2, 1]]
    # output: [2,1]
    # EXPLANATION:   Since there is exactly one odd index and one even index, no rearrangement of values takes place. The resultant array formed is [2,1], which is the same as the initial array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortEvenOdd 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    a = sorted(nums[::2])
    b = sorted(nums[1::2], reverse=True)
    nums[::2] = a
    nums[1::2] = b
    return nums
"-----------------"
test()

