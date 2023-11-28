### findKthPositive 
from typing import *
def f_gold(arr: List[int], k: int) -> int:
    if arr[0] > k:
        return k
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) >> 1
        if arr[mid] - mid - 1 >= k:
            right = mid
        else:
            left = mid + 1
    return arr[left - 1] + k - (arr[left - 1] - (left - 1) - 1)