### numberOfWeeks 
from typing import *
def f_gold(milestones: List[int]) -> int:
    mx, s = max(milestones), sum(milestones)
    rest = s - mx
    return rest * 2 + 1 if mx > rest + 1 else s