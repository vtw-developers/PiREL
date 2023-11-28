### cellsInRange 
from typing import *
def f_gold(s: str) -> List[str]:
    return [
        chr(i) + str(j)
        for i in range(ord(s[0]), ord(s[-2]) + 1)
        for j in range(int(s[1]), int(s[-1]) + 1)
    ]