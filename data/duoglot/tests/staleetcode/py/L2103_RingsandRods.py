
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["B0B6G0R6R0R6G9"]
    # output: 1
    # EXPLANATION:   - The rod labeled 0 holds 3 rings with all colors: red, green, and blue. - The rod labeled 6 holds 3 rings, but it only has red and blue. - The rod labeled 9 holds only a green ring. Thus, the number of rods with all three colors is 1.
    ,
    # example 2
    ["B0R0G0R9R0B0G0"]
    # output: 1
    # EXPLANATION:   - The rod labeled 0 holds 6 rings with all colors: red, green, and blue. - The rod labeled 9 holds only a red ring. Thus, the number of rods with all three colors is 1.
    ,
    # example 3
    ["G4"]
    # output: 0
    # EXPLANATION:   Only one ring is given. Thus, no rods have all three colors.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countPoints 
from collections import defaultdict
from typing import *
def f_gold(rings: str) -> int:
    mp = defaultdict(set)
    for i in range(1, len(rings), 2):
        c = int(rings[i])
        mp[c].add(rings[i - 1])
    return sum(len(v) == 3 for v in mp.values())
"-----------------"
test()

