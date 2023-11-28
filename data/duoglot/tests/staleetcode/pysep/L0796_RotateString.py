### rotateString 
from typing import *
def f_gold(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s