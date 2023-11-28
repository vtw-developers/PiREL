
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]]
    # output: true
    # EXPLANATION:  Perform the following operations: - Choose the first and last triplets [<u>[2,5,3]</u>,[1,8,4],<u>[1,7,5]</u>]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],<u>[2,7,5]</u>] The target triplet [2,7,5] is now an element of triplets.
    ,
    # example 2
    [[[3, 4, 5], [4, 5, 6]], [3, 2, 5]]
    # output: false
    # EXPLANATION:  It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
    ,
    # example 3
    [[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]]
    # output: true
    # EXPLANATION: Perform the following operations: - Choose the first and third triplets [<u>[2,5,3]</u>,[2,3,4],<u>[1,2,5]</u>,[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],<u>[2,5,5]</u>,[5,2,3]]. - Choose the third and fourth triplets [[2,5,3],[2,3,4],<u>[2,5,5]</u>,<u>[5,2,3]</u>]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],<u>[5,5,5]</u>]. The target triplet [5,5,5] is now an element of triplets.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### mergeTriplets 
from typing import *
def f_gold(triplets: List[List[int]], target: List[int]) -> bool:
    maxA = maxB = maxC = 0
    tA, tB, tC = target
    for a, b, c in triplets:
        if a <= tA and b <= tB and c <= tC:
            maxA = max(maxA, a)
            maxB = max(maxB, b)
            maxC = max(maxC, c)
    return (maxA, maxB, maxC) == (tA, tB, tC)
"-----------------"
test()

