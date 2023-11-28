
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 4, 2, 6, 8]]
    # output: [1,3,4]
    # EXPLANATION:  One possible original array could be [1,3,4]: - Twice the value of 1 is 1 * 2 = 2. - Twice the value of 3 is 3 * 2 = 6. - Twice the value of 4 is 4 * 2 = 8. Other original arrays could be [4,3,1] or [3,1,4].
    ,
    # example 2
    [[6, 3, 0, 1]]
    # output: []
    # EXPLANATION:  changed is not a doubled array.
    ,
    # example 3
    [[1]]
    # output: []
    # EXPLANATION:  changed is not a doubled array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findOriginalArray 
from typing import *
def f_gold(changed: List[int]) -> List[int]:
    if len(changed) % 2 != 0:
        return []
    n = 100010
    counter = [0] * n
    for x in changed:
        counter[x] += 1
    if counter[0] % 2 != 0:
        return []
    res = [0] * (counter[0] // 2)
    for i in range(1, n):
        if counter[i] == 0:
            continue
        if i * 2 > n or counter[i] > counter[i * 2]:
            return []
        res.extend([i] * counter[i])
        counter[i * 2] -= counter[i]
    return res
"-----------------"
test()

