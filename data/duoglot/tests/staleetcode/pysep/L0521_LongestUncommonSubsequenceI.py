### findLUSlength 
from typing import *
def f_gold(a: str, b: str) -> int:
    return -1 if a == b else max(len(a), len(b))