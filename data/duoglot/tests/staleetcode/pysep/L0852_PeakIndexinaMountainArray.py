### peakIndexInMountainArray 
from typing import *
def f_gold(arr: List[int]) -> int:
    left, right = 1, len(arr) - 2
    while left < right:
        mid = (left + right) >> 1
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left