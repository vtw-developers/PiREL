### kthGrammar 
from typing import *
def f_gold(n: int, k: int) -> int:
    if n == 1:
        return 0
    if k <= (1 << (n - 2)):
        return f_gold(n - 1, k)
    return f_gold(n - 1, k - (1 << (n - 2))) ^ 1