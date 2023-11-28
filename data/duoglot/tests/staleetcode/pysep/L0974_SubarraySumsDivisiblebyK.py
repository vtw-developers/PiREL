### subarraysDivByK 
from collections import Counter
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    ans = s = 0
    counter = Counter({0: 1})
    for num in nums:
        s += num
        ans += counter[s % k]
        counter[s % k] += 1
    return ans