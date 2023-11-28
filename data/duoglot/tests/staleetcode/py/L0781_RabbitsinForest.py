
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2]]
    # output: 5
    # EXPLANATION:  The two rabbits that answered "1" could both be the same color, say red. The rabbit that answered "2" can't be red or the answers would be inconsistent. Say the rabbit that answered "2" was blue. Then there should be 2 other blue rabbits in the forest that didn't answer into the array. The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
    ,
    # example 2
    [[10, 10, 10]]
    # output: 11
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numRabbits 
import math
from math import ceil
from collections import Counter
from typing import *
def f_gold(answers: List[int]) -> int:
    counter = Counter(answers)
    return sum([math.ceil(v / (k + 1)) * (k + 1) for k, v in counter.items()])
"-----------------"
test()

