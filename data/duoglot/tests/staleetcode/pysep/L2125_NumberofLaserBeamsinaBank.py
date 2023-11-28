### numberOfBeams 
from typing import *
def f_gold(bank: List[str]) -> int:
    last = ans = 0
    for b in bank:
        if (t := b.count('1')) > 0:
            ans += last * t
            last = t
    return ans