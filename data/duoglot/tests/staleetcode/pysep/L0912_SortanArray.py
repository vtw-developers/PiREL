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