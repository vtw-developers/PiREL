### removeDigit 
from typing import *
def f_gold(number: str, digit: str) -> str:
    return max(
        number[:i] + number[i + 1 :] for i, d in enumerate(number) if d == digit
    )