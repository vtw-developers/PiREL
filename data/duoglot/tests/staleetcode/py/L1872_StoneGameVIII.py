
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, 2, -3, 4, -5]]
    # output: 5
    # EXPLANATION:   - Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of    value 2 on the left. stones = [2,-5].  - Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on    the left. stones = [-3].  The difference between their scores is 2 - (-3) = 5.
    ,
    # example 2
    [[7, -6, 5, 10, 5, -2, -6]]
    # output: 13
    # EXPLANATION:   - Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a    stone of value 13 on the left. stones = [13].  The difference between their scores is 13 - 0 = 13.
    ,
    # example 3
    [[-10, -12]]
    # output: -22
    # EXPLANATION:   - Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her    score and places a stone of value -22 on the left. stones = [-22].  The difference between their scores is (-22) - 0 = -22.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### stoneGameVIII 
from itertools import accumulate
from typing import *
def f_gold(stones: List[int]) -> int:
    pre_sum = list(accumulate(stones))
    f = pre_sum[len(stones) - 1]
    for i in range(len(stones) - 2, 0, -1):
        f = max(f, pre_sum[i] - f)
    return f
"-----------------"
test()

