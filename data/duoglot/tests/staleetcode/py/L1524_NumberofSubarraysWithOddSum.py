
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5]]
    # output: 4
    # EXPLANATION:  All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]] All sub-arrays sum are [1,4,9,3,8,5]. Odd sums are [1,9,3,5] so the answer is 4.
    ,
    # example 2
    [[2, 4, 6]]
    # output: 0
    # EXPLANATION:  All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]] All sub-arrays sum are [2,6,12,4,10,6]. All sub-arrays have even sum and the answer is 0.
    ,
    # example 3
    [[1, 2, 3, 4, 5, 6, 7]]
    # output: 16
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numOfSubarrays 
from typing import *
def f_gold(arr: List[int]) -> int:
    MOD = int(1e9) + 7
    counter = [0] * 2
    s = ans = 0
    for v in arr:
        s += v
        counter[s % 2] += 1
        if s % 2 == 1:
            ans += 1 + counter[0]
        else:
            ans += counter[1]
    return ans % MOD
"-----------------"
test()

