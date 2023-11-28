
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 3, 5, 6]]
    # output: 3
    # EXPLANATION:  [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
    ,
    # example 2
    [[1, 2, 100]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hIndex 
from typing import *
def f_gold(citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n
    while left < right:
        mid = (left + right + 1) >> 1
        if citations[n - mid] >= mid:
            left = mid
        else:
            right = mid - 1
    return left
"-----------------"
test()

