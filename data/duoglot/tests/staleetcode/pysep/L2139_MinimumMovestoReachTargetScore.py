### minMoves 
from typing import *
def f_gold(target: int, maxDoubles: int) -> int:
    if target == 1:
        return 0
    if maxDoubles == 0:
        return target - 1
    if target % 2 == 0 and maxDoubles:
        return 1 + f_gold(target >> 1, maxDoubles - 1)
    return 1 + f_gold(target - 1, maxDoubles)