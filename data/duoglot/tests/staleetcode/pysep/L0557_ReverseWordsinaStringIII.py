### reverseWords 
from typing import *
def f_gold(s: str) -> str:
    return ' '.join([t[::-1] for t in s.split(' ')])