### reverseWords 
from typing import *
def f_gold(s: str) -> str:
    words = s.strip().split()
    return ' '.join(words[::-1])