### addDigits 
from typing import *
def f_gold(num: int) -> int:
    return 0 if num == 0 else (num - 1) % 9 + 1