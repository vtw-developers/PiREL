### areNumbersAscending 
from typing import *
def f_gold(s: str) -> bool:
    curr = 0
    for t in s.split(' '):
        if t[0].isdigit():
            if curr >= int(t):
                return False
            curr = int(t)
    return True