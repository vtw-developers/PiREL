### findPoisonedDuration 
from typing import *
def f_gold(timeSeries: List[int], duration: int) -> int:
    n, res = len(timeSeries), duration
    for i in range(n - 1):
        res += min(duration, timeSeries[i + 1] - timeSeries[i])
    return res