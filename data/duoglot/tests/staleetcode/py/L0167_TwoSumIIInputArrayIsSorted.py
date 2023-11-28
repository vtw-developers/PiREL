
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 7, 11, 15], 9]
    # output: [1,2]
    # EXPLANATION:  The sum of 2 and 7 is 9. Therefore, index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
    ,
    # example 2
    [[2, 3, 4], 6]
    # output: [1,3]
    # EXPLANATION:  The sum of 2 and 4 is 6. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 3. We return [1, 3].
    ,
    # example 3
    [[-1, 0], -1]
    # output: [1,2]
    # EXPLANATION:  The sum of -1 and 0 is -1. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### twoSum 
from typing import *
def f_gold(numbers: List[int], target: int) -> List[int]:
    i, j = 1, len(numbers)
    while i < j:
        x = numbers[i - 1] + numbers[j - 1]
        if x == target:
            return [i, j]
        if x < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]
"-----------------"
test()

