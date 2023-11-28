### findDifference 
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1, s2 = set(nums1), set(nums2)
    return [list(s1 - s2), list(s2 - s1)]