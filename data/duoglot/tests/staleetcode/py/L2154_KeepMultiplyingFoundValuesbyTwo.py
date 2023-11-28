
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 3, 6, 1, 12], 3]
    # output: 24
    # EXPLANATION:   - 3 is found in nums. 3 is multiplied by 2 to obtain 6. - 6 is found in nums. 6 is multiplied by 2 to obtain 12. - 12 is found in nums. 12 is multiplied by 2 to obtain 24. - 24 is not found in nums. Thus, 24 is returned.
    ,
    # example 2
    [[2, 7, 9], 4]
    # output: 4
    # EXPLANATION:  - 4 is not found in nums. Thus, 4 is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findFinalValue 
from typing import *
def f_gold(nums: List[int], original: int) -> int:
    s = set(nums)
    while original in s:
        original <<= 1
    return original
"-----------------"
test()

