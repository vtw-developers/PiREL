### subarraySum 
from collections import Counter
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    counter = Counter({0: 1})
    ans = s = 0
    for num in nums:
        s += num
        ans += counter[s - k]
        counter[s] += 1
    return ans