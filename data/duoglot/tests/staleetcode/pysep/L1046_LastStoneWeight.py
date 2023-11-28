### lastStoneWeight 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(stones: List[int]) -> int:
    h = [-s for s in stones]
    heapify(h)
    while len(h) > 1:
        y, x = -heappop(h), -heappop(h)
        if x != y:
            heappush(h, x - y)
    return 0 if not h else -h[0]