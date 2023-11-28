
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["110"]
    # output: [1,1,3]
    # EXPLANATION:  The answer for each box is as follows: 1) First box: you will have to move one ball from the second box to the first box in one operation. 2) Second box: you will have to move one ball from the first box to the second box in one operation. 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
    ,
    # example 2
    ["001011"]
    # output: [11,8,5,4,3,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minOperations 
from typing import *
def f_gold(boxes: str) -> List[int]:
    n = len(boxes)
    res = [0] * n
    total = 0
    for i, b in enumerate(boxes):
        if b == '1':
            res[0] += i
            total += 1
    left, right = 0, total
    for i in range(1, n):
        if boxes[i - 1] == '1':
            left += 1
            right -= 1
        res[i] = res[i - 1] + left - right
    return res
"-----------------"
test()

