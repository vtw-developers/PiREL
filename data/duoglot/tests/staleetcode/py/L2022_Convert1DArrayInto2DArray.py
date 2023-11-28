
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], 2, 2]
    # output: [[1,2],[3,4]]
    # EXPLANATION:  The constructed 2D array should contain 2 rows and 2 columns. The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array. The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
    ,
    # example 2
    [[1, 2, 3], 1, 3]
    # output: [[1,2,3]]
    # EXPLANATION:  The constructed 2D array should contain 1 row and 3 columns. Put all three elements in original into the first row of the constructed 2D array.
    ,
    # example 3
    [[1, 2], 1, 1]
    # output: []
    # EXPLANATION:  There are 2 elements in original. It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### construct2DArray 
from typing import *
def f_gold(original: List[int], m: int, n: int) -> List[List[int]]:
    if m * n != len(original):
        return []
    return [original[i : i + n] for i in range(0, m * n, n)]
"-----------------"
test()

