### numRescueBoats 
from typing import *
def f_gold(people: List[int], limit: int) -> int:
    people.sort()
    num, i, j = 0, 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        num += 1
    return num