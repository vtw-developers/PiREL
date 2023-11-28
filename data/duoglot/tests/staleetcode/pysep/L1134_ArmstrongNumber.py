### isArmstrong 
from typing import *
def f_gold(n: int) -> bool:
    k = len(str(n))
    s, t = 0, n
    while t:
        t, v = divmod(t, 10)
        s += pow(v, k)
    return n == s