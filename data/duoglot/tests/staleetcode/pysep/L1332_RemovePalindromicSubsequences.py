### removePalindromeSub 
from typing import *
def f_gold(s: str) -> int:
    if not s:
        return 0
    if s[::-1] == s:
        return 1
    return 2