### reverseString 
from typing import *
def f_gold(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]