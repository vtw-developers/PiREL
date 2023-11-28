
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[17, 18, 5, 4, 6, 1]]
    # output: [18,6,6,6,1,-1]
    # EXPLANATION:   - index 0 --> the greatest element to the right of index 0 is index 1 (18). - index 1 --> the greatest element to the right of index 1 is index 4 (6). - index 2 --> the greatest element to the right of index 2 is index 4 (6). - index 3 --> the greatest element to the right of index 3 is index 4 (6). - index 4 --> the greatest element to the right of index 4 is index 5 (1). - index 5 --> there are no elements to the right of index 5, so we put -1.
    ,
    # example 2
    [[400]]
    # output: [-1]
    # EXPLANATION:  There are no elements to the right of index 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### replaceElements 
from typing import *
def f_gold(arr: List[int]) -> List[int]:
    m = -1
    for i in range(len(arr) - 1, -1, -1):
        t = arr[i]
        arr[i] = m
        m = max(m, t)
    return arr
"-----------------"
test()

