
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[15, 88], [[88], [15]]]
    # output: true
    # EXPLANATION:  Concatenate [15] then [88]
    ,
    # example 2
    [[49, 18, 16], [[16, 18, 49]]]
    # output: false
    # EXPLANATION:  Even though the numbers match, we cannot reorder pieces[0].
    ,
    # example 3
    [[91, 4, 64, 78], [[78], [4, 64], [91]]]
    # output: true
    # EXPLANATION:  Concatenate [91] then [4,64] then [78]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canFormArray 
from typing import *
def f_gold(arr: List[int], pieces: List[List[int]]) -> bool:
    mapper = {piece[0]: piece for piece in pieces}
    i, n = 0, len(arr)
    while i < n:
        if arr[i] not in mapper:
            return False
        vals = mapper[arr[i]]
        for val in vals:
            if arr[i] != val:
                return False
            i += 1
    return True
"-----------------"
test()

