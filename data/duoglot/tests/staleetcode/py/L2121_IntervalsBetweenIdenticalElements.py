
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 3, 1, 2, 3, 3]]
    # output: [4,2,7,2,4,4,5]
    # EXPLANATION:  - Index 0: Another 2 is found at index 4. |0 - 4| = 4 - Index 1: Another 1 is found at index 3. |1 - 3| = 2 - Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7 - Index 3: Another 1 is found at index 1. |3 - 1| = 2 - Index 4: Another 2 is found at index 0. |4 - 0| = 4 - Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4 - Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
    ,
    # example 2
    [[10, 5, 10, 10]]
    # output: [5,0,3,4]
    # EXPLANATION:  - Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5 - Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0. - Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3 - Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getDistances 
from collections import defaultdict
from typing import *
def f_gold(arr: List[int]) -> List[int]:
    d = defaultdict(list)
    n = len(arr)
    for i, v in enumerate(arr):
        d[v].append(i)
    ans = [0] * n
    for v in d.values():
        m = len(v)
        val = sum(v) - v[0] * m
        for i, p in enumerate(v):
            delta = v[i] - v[i - 1] if i >= 1 else 0
            val += i * delta - (m - i) * delta
            ans[p] = val
    return ans
"-----------------"
test()

