### totalMoney 
from typing import *
def f_gold(n: int) -> int:
    a, b = divmod(n, 7)
    return (28 + 28 + 7 * (a - 1)) * a // 2 + (a * 2 + b + 1) * b // 2