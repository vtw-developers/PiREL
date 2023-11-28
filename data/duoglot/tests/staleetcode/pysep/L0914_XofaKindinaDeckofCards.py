### hasGroupsSizeX 
from functools import reduce
import math
from math import gcd
from collections import Counter
from typing import *
def f_gold(deck: List[int]) -> bool:
    vals = Counter(deck).values()
    return reduce(gcd, vals) >= 2