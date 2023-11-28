### minStoneSum 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(piles: List[int], k: int) -> int:
    h = []
    for p in piles:
        heappush(h, -p)
    for _ in range(k):
        p = -heappop(h)
        heappush(h, -((p + 1) >> 1))
    return -sum(h)