### grayCode 
from typing import *
def f_gold(n: int) -> List[int]:
    return [i ^ (i >> 1) for i in range(1 << n)]