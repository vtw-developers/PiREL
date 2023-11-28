### sumOfThree 
from typing import *
def f_gold(num: int) -> List[int]:
    a, b = divmod(num, 3)
    return [] if b else [a - 1, a, a + 1]