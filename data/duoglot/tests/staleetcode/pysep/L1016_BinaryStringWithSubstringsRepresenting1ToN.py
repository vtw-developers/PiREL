### queryString 
from typing import *
def f_gold(s: str, n: int) -> bool:
    for i in range(n, n // 2, -1):
        if bin(i)[2:] not in s:
            return False
    return True