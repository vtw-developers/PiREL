### hasAllCodes 
from typing import *
def f_gold(s: str, k: int) -> bool:
    counter = 1 << k
    exists = set()
    for i in range(k, len(s) + 1):
        if s[i - k : i] not in exists:
            exists.add(s[i - k : i])
            counter -= 1
        if counter == 0:
            return True
    return False