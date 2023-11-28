### dailyTemperatures 
from typing import *
def f_gold(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stk = []
    for i, t in enumerate(temperatures):
        while stk and temperatures[stk[-1]] < t:
            j = stk.pop()
            ans[j] = i - j
        stk.append(i)
    return ans