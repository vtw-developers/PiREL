
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 0, 1, 1, 9, 7], 7, 2, 3]
    # output: 4
    # EXPLANATION:  There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
    ,
    # example 2
    [[1, 1, 2, 2, 3], 0, 0, 1]
    # output: 0
    # EXPLANATION: No triplet satisfies all conditions.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countGoodTriplets 
from typing import *
def f_gold(arr: List[int], a: int, b: int, c: int) -> int:
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (
                    abs(arr[i] - arr[j]) <= a
                    and abs(arr[j] - arr[k]) <= b
                    and abs(arr[i] - arr[k]) <= c
                ):
                    ans += 1
    return ans
"-----------------"
test()

