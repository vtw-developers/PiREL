### findKthNumber 
from typing import *
def f_gold(m: int, n: int, k: int) -> int:
    left, right = 1, m * n
    while left < right:
        mid = (left + right) >> 1
        cnt = 0
        for i in range(1, m + 1):
            cnt += min(mid // i, n)
        if cnt >= k:
            right = mid
        else:
            left = mid + 1
    return left