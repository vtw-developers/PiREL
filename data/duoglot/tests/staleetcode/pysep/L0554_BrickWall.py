### leastBricks 
from collections import defaultdict
from typing import *
def f_gold(wall: List[List[int]]) -> int:
    cnt = defaultdict(int)
    for row in wall:
        width = 0
        for brick in row[:-1]:
            width += brick
            cnt[width] += 1
    if not cnt:
        return len(wall)
    return len(wall) - cnt[max(cnt, key=cnt.get)]