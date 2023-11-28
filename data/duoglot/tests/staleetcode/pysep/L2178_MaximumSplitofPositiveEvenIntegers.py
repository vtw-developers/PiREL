### maximumEvenSplit 
from typing import *
def f_gold(finalSum: int) -> List[int]:
    if finalSum % 2:
        return []
    i = 2
    ans = []
    while i <= finalSum:
        ans.append(i)
        finalSum -= i
        i += 2
    ans[-1] += finalSum
    return ans