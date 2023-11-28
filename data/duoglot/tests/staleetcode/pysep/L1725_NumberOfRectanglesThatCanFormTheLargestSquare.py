### countGoodRectangles 
from typing import *
def f_gold(rectangles: List[List[int]]) -> int:
    ans = mx = 0
    for l, w in rectangles:
        t = min(l, w)
        if mx < t:
            mx, ans = t, 1
        elif mx == t:
            ans += 1
    return ans