### frequencySort 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    cnt = Counter(nums)
    cnt = sorted(cnt.items(), key=lambda x: (x[1], -x[0]))
    ans = []
    for v, freq in cnt:
        ans.extend([v] * freq)
    return ans