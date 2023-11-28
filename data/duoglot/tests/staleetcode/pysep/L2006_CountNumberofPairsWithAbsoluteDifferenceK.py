### countKDifference 
from collections import Counter
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    ans = 0
    counter = Counter()
    for num in nums:
        ans += counter[num - k] + counter[num + k]
        counter[num] += 1
    return ans