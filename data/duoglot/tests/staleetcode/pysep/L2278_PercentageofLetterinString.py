### percentageLetter 
from typing import *
def f_gold(s: str, letter: str) -> int:
    return s.count(letter) * 100 // len(s)