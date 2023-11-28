
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5]
    # output: true
    # EXPLANATION:  Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
    ,
    # example 2
    [[1, 2, 3, 4, 5, 6], 7]
    # output: true
    # EXPLANATION:  Pairs are (1,6),(2,5) and(3,4).
    ,
    # example 3
    [[1, 2, 3, 4, 5, 6], 10]
    # output: false
    # EXPLANATION:  You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canArrange 
from typing import *
def f_gold(arr: List[int], k: int) -> bool:
    mod = [0] * k
    for v in arr:
        mod[v % k] += 1
    return all(mod[i] == mod[k - i] for i in range(1, k)) and mod[0] % 2 == 0
"-----------------"
test()

