### numRabbits 
import math
from math import ceil
from collections import Counter
from typing import *
def f_gold(answers: List[int]) -> int:
    counter = Counter(answers)
    return sum([math.ceil(v / (k + 1)) * (k + 1) for k, v in counter.items()])