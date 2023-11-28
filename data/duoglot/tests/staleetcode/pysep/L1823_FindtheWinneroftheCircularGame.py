### findTheWinner 
from typing import *
def f_gold(n: int, k: int) -> int:
    if n == 1:
        return 1
    ans = (k + f_gold(n - 1, k)) % n
    return n if ans == 0 else ans