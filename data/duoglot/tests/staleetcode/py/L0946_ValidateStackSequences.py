
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]]
    # output: true
    # EXPLANATION:  We might do the following sequence: push(1), push(2), push(3), push(4), pop() -> 4, push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
    ,
    # example 2
    [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]]
    # output: false
    # EXPLANATION:  1 cannot be popped before 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### validateStackSequences 
from typing import *
def f_gold(pushed: List[int], popped: List[int]) -> bool:
    stk, j, n = [], 0, len(popped)
    for x in pushed:
        stk.append(x)
        while stk and j < n and stk[-1] == popped[j]:
            stk.pop()
            j += 1
    return j == n
"-----------------"
test()

