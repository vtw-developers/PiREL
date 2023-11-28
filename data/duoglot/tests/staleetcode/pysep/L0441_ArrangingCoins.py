### arrangeCoins 
import math
from math import sqrt
from typing import *
def f_gold(n: int) -> int:
    return int(math.sqrt(2) * math.sqrt(n + 0.125) - 0.5)