### maximumPopulation 
from typing import *
def f_gold(logs: List[List[int]]) -> int:
    delta = [0] * 2055
    for birth, death in logs:
        delta[birth] += 1
        delta[death] -= 1
    mx = res = cur = 0
    for i, v in enumerate(delta):
        cur += v
        if mx < cur:
            mx = cur
            res = i
    return res