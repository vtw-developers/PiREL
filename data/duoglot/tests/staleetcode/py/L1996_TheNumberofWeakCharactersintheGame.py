
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[5, 5], [6, 3], [3, 6]]]
    # output: 0
    # EXPLANATION:  No character has strictly greater attack and defense than the other.
    ,
    # example 2
    [[[2, 2], [3, 3]]]
    # output: 1
    # EXPLANATION:  The first character is weak because the second character has a strictly greater attack and defense.
    ,
    # example 3
    [[[1, 5], [10, 4], [4, 3]]]
    # output: 1
    # EXPLANATION:  The third character is weak because the second character has a strictly greater attack and defense.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfWeakCharacters 
from typing import *
def f_gold(properties: List[List[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))
    ans = mx = 0
    for _, d in properties:
        if mx > d:
            ans += 1
        mx = max(mx, d)
    return ans
"-----------------"
test()

