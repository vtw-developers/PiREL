### groupThePeople 
from collections import defaultdict
from typing import *
def f_gold(groupSizes: List[int]) -> List[List[int]]:
    mp = defaultdict(list)
    for i, x in enumerate(groupSizes):
        mp[x].append(i)
    res = []
    for x, indexes in mp.items():
        l = len(indexes)
        for i in range(0, l, x):
            res.append(indexes[i : i + x])
    return res