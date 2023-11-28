### addBinary 
from typing import *
def f_gold(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]