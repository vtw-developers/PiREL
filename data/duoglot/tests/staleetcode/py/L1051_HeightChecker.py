
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 4, 2, 1, 3]]
    # output: 3
    # EXPLANATION:   heights:  [1,1,<u>4</u>,2,<u>1</u>,<u>3</u>] expected: [1,1,<u>1</u>,2,<u>3</u>,<u>4</u>] Indices 2, 4, and 5 do not match.
    ,
    # example 2
    [[5, 1, 2, 3, 4]]
    # output: 5
    # EXPLANATION:  heights:  [<u>5</u>,<u>1</u>,<u>2</u>,<u>3</u>,<u>4</u>] expected: [<u>1</u>,<u>2</u>,<u>3</u>,<u>4</u>,<u>5</u>] All indices do not match.
    ,
    # example 3
    [[1, 2, 3, 4, 5]]
    # output: 0
    # EXPLANATION:  heights:  [1,2,3,4,5] expected: [1,2,3,4,5] All indices match.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### heightChecker 
from typing import *
def f_gold(heights: List[int]) -> int:
    expected = sorted(heights)
    return sum(a != b for a, b in zip(heights, expected))
"-----------------"
test()

