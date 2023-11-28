
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5]
    # output: 15
    # EXPLANATION:  A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:  1st day: 1, 2, 3, 4, 5  2nd day: 6, 7  3rd day: 8  4th day: 9  5th day: 10    Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
    ,
    # example 2
    [[3, 2, 2, 4, 1, 4], 3]
    # output: 6
    # EXPLANATION:  A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:  1st day: 3, 2  2nd day: 2, 4  3rd day: 1, 4
    ,
    # example 3
    [[1, 2, 3, 1, 1], 4]
    # output: 3
    # EXPLANATION:   1st day: 1  2nd day: 2  3rd day: 3  4th day: 1, 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shipWithinDays 
from typing import *
def f_gold(weights: List[int], D: int) -> int:
    def check(capacity):
        cnt, t = 1, 0
        for w in weights:
            if w > capacity:
                return False
            if t + w <= capacity:
                t += w
            else:
                cnt += 1
                t = w
        return cnt <= D
    left, right = 1, 25000000
    while left < right:
        mid = (left + right) >> 1
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

