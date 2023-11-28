### busyStudent 
from typing import *
def f_gold(startTime: List[int], endTime: List[int], queryTime: int
) -> int:
    count, n = 0, len(startTime)
    for i in range(n):
        count += startTime[i] <= queryTime <= endTime[i]
    return count