
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6, [11, 6]]
    # output: 3
    # EXPLANATION:  One optimal way is: - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3 - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3 The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.
    ,
    # example 2
    [7, [15, 10, 10]]
    # output: 5
    # EXPLANATION:  One optimal way is: - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5 - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5 - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5 The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.
    ,
    # example 3
    [1, [100000]]
    # output: 100000
    # EXPLANATION:  The only optimal way is: - The 100000 products of type 0 are distributed to the only store. The maximum number of products given to any store is max(100000) = 100000.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimizedMaximum 
from typing import *
def f_gold(n: int, quantities: List[int]) -> int:
    left, right = 1, int(1e5)
    while left < right:
        mid = (left + right) >> 1
        s = sum([(q + mid - 1) // mid for q in quantities])
        if s <= n:
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

