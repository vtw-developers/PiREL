### findGCD 
import math
from math import gcd
from typing import *
def f_gold(nums: List[int]) -> int:
    return gcd(max(nums), min(nums))