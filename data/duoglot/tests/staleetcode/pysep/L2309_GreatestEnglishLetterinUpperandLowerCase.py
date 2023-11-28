### greatestLetter 
from string import ascii_uppercase
from typing import *
def f_gold(s: str) -> str:
    ss = set(s)
    for c in ascii_uppercase[::-1]:
        if c in ss and c.lower() in ss:
            return c
    return ''