### minMovesToSeat 
from typing import *
def f_gold(seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()
    return sum(abs(seats[i] - students[i]) for i in range(len(seats)))