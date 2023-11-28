### largestOddNumber 
from typing import *
def f_gold(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if (int(num[i]) & 1) == 1:
            return num[: i + 1]
    return ''