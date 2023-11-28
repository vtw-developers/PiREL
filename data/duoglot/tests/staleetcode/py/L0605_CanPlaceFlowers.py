
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 0, 0, 1], 1]
    # output: true
    ,
    # example 2
    [[1, 0, 0, 0, 1], 2]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canPlaceFlowers 
from typing import *
def f_gold(flowerBed, n):
    """
    type flowerBed : List[int], n : int
    rtype : bool
    """
    i = 0
    while n > 0 and i < len(flowerBed):
        if i == 0 and flowerBed[0] == 0:  # for 1st Element
            if len(flowerBed) == 1 or (len(flowerBed) > 1 and flowerBed[1] == 0):
                n -= 1
                flowerBed[0] = 1
        elif (
            i == len(flowerBed) - 1 and flowerBed[i] == 0 and flowerBed[i - 1] == 0
        ):  # for last element
            n -= 1
            flowerBed[i] = 1
        elif flowerBed[i] == 0 and flowerBed[i - 1] == 0 and flowerBed[i + 1] == 0:
            n -= 1
            flowerBed[i] = 1
        i += 1
    return n == 0
"-----------------"
test()

