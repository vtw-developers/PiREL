### isThree 
from typing import *
def f_gold(n: int) -> bool:
    return sum(n % i == 0 for i in range(2, n)) == 1