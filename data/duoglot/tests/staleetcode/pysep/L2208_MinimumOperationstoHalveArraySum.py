### halveArray 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(nums: List[int]) -> int:
    s = sum(nums) / 2
    h = []
    for v in nums:
        heappush(h, -v)
    ans = 0
    while s > 0:
        t = -heappop(h) / 2
        s -= t
        heappush(h, -t)
        ans += 1
    return ans