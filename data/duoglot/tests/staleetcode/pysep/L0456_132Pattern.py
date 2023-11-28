### find132pattern 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> bool:
    ak = float('-inf')
    stack = []
    for num in nums[::-1]:
        if num < ak:
            return True
        while stack and num > stack[-1]:
            ak = stack.pop()
        stack.append(num)
    return False