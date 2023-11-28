
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3], [2]]
    # output: 1
    # EXPLANATION:  The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
    ,
    # example 2
    [[1, 2, 3, 4], [1, 4]]
    # output: 1
    # EXPLANATION:  The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
    ,
    # example 3
    [[1, 5], [2]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findRadius 
from typing import *
def f_gold(houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()
    def check(r):
        m, n = len(houses), len(heaters)
        i = j = 0
        while i < m:
            if j >= n:
                return False
            mi = heaters[j] - r
            mx = heaters[j] + r
            if houses[i] < mi:
                return False
            if houses[i] > mx:
                j += 1
            else:
                i += 1
        return True
    left, right = 0, int(1e9)
    while left < right:
        mid = (left + right) >> 1
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

