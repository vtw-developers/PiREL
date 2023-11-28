
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5]
    # output: [10,55,45,25,25]
    # EXPLANATION:  Flight labels:        1   2   3   4   5 Booking 1 reserved:  10  10 Booking 2 reserved:      20  20 Booking 3 reserved:      25  25  25  25 Total seats:         10  55  45  25  25 Hence, answer = [10,55,45,25,25]
    ,
    # example 2
    [[[1, 2, 10], [2, 2, 15]], 2]
    # output: [10,25]
    # EXPLANATION:  Flight labels:        1   2 Booking 1 reserved:  10  10 Booking 2 reserved:      15 Total seats:         10  25 Hence, answer = [10,25]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
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
"-----------------"
test()

