### anagramMappings 
from collections import defaultdict
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> List[int]:
    mapper = defaultdict(set)
    for i, num in enumerate(nums2):
        mapper[num].add(i)
    return [mapper[num].pop() for num in nums1]