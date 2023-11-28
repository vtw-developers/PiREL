### generateTheString 
from typing import *
def f_gold(n: int) -> str:
    return 'a' * n if n & 1 else 'a' * (n - 1) + 'b'