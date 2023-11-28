
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 1, 5, 6, 4], 2]
    # output: 5
    ,
    # example 2
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findKthLargest 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    def quick_sort(left, right, k):
        if left == right:
            return nums[left]
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
        if j < k:
            return quick_sort(j + 1, right, k)
        return quick_sort(left, j, k)
    n = len(nums)
    return quick_sort(0, n - 1, n - k)
"-----------------"
test()

