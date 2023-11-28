
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 2, 3, 1]]
    # output: [1,2,3,5]
    ,
    # example 2
    [[5, 1, 1, 2, 0, 0]]
    # output: [0,0,1,1,2,5]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortArray 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    def quick_sort(nums, left, right):
        if left >= right:
            return
        i, j = left - 1, right + 1
        x = nums[(left + right) >> 1]
        while i < j:
            while 1:
                i += 1
                if nums[i] >= x:
                    break
            while 1:
                j -= 1
                if nums[j] <= x:
                    break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        quick_sort(nums, left, j)
        quick_sort(nums, j + 1, right)
    quick_sort(nums, 0, len(nums) - 1)
    return nums
"-----------------"
test()

