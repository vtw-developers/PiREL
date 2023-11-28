### corpFlightBookings 
from itertools import accumulate
from typing import *
def f_gold(bookings: List[List[int]], n: int) -> List[int]:
    delta = [0] * n
    for first, last, seats in bookings:
        delta[first - 1] += seats
        if last < n:
            delta[last] -= seats
    return list(accumulate(delta))