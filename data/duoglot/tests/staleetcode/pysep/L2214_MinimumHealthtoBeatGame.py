### minimumHealth 
from typing import *
def f_gold(damage: List[int], armor: int) -> int:
    return sum(damage) - min(max(damage), armor) + 1