### powerfulIntegers 
from typing import *
def f_gold(x: int, y: int, bound: int) -> List[int]:
    s = set()
    i = 1
    while i < bound:
        j = 1
        while j < bound:
            if i + j <= bound:
                s.add(i + j)
            if y == 1:
                break
            j *= y
        if x == 1:
            break
        i *= x
    return list(s)