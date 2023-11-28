### kthDistinct 
from collections import Counter
from typing import *
def f_gold(arr: List[str], k: int) -> str:
    counter = Counter(arr)
    for v in arr:
        if counter[v] == 1:
            k -= 1
            if k == 0:
                return v
    return ''