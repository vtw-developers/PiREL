### countCollisions 
from typing import *
def f_gold(directions: str) -> int:
    d = directions.lstrip('L').rstrip('R')
    return len(d) - d.count('S')