### intersect 
from collections import Counter
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> List[int]:
    counter = Counter(nums1)
    res = []
    for num in nums2:
        if counter[num] > 0:
            res.append(num)
            counter[num] -= 1
    return res