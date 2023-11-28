
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 0, 1, 0]]
    # output: [2,4]
    # EXPLANATION:  Division at index - 0: nums<sub>left</sub> is []. nums<sub>right</sub> is [0,0,<u><strong>1</strong></u>,0]. The score is 0 + 1 = 1. - 1: nums<sub>left</sub> is [<u><strong>0</strong></u>]. nums<sub>right</sub> is [0,<u><strong>1</strong></u>,0]. The score is 1 + 1 = 2. - 2: nums<sub>left</sub> is [<u><strong>0</strong></u>,<u><strong>0</strong></u>]. nums<sub>right</sub> is [<u><strong>1</strong></u>,0]. The score is 2 + 1 = 3. - 3: nums<sub>left</sub> is [<u><strong>0</strong></u>,<u><strong>0</strong></u>,1]. nums<sub>right</sub> is [0]. The score is 2 + 0 = 2. - 4: nums<sub>left</sub> is [<u><strong>0</strong></u>,<u><strong>0</strong></u>,1,<u><strong>0</strong></u>]. nums<sub>right</sub> is []. The score is 3 + 0 = 3. Indices 2 and 4 both have the highest possible division score 3. Note the answer [4,2] would also be accepted.
    ,
    # example 2
    [[0, 0, 0]]
    # output: [3]
    # EXPLANATION:  Division at index - 0: nums<sub>left</sub> is []. nums<sub>right</sub> is [0,0,0]. The score is 0 + 0 = 0. - 1: nums<sub>left</sub> is [<u><strong>0</strong></u>]. nums<sub>right</sub> is [0,0]. The score is 1 + 0 = 1. - 2: nums<sub>left</sub> is [<u><strong>0</strong></u>,<u><strong>0</strong></u>]. nums<sub>right</sub> is [0]. The score is 2 + 0 = 2. - 3: nums<sub>left</sub> is [<u><strong>0</strong></u>,<u><strong>0</strong></u>,<u><strong>0</strong></u>]. nums<sub>right</sub> is []. The score is 3 + 0 = 3. Only index 3 has the highest possible division score 3.
    ,
    # example 3
    [[1, 1]]
    # output: [0]
    # EXPLANATION:  Division at index - 0: nums<sub>left</sub> is []. nums<sub>right</sub> is [<u><strong>1</strong></u>,<u><strong>1</strong></u>]. The score is 0 + 2 = 2. - 1: nums<sub>left</sub> is [1]. nums<sub>right</sub> is [<u><strong>1</strong></u>]. The score is 0 + 1 = 1. - 2: nums<sub>left</sub> is [1,1]. nums<sub>right</sub> is []. The score is 0 + 0 = 0. Only index 0 has the highest possible division score 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxScoreIndices 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    left, right = 0, sum(nums)
    mx = right
    ans = [0]
    for i, num in enumerate(nums):
        if num == 0:
            left += 1
        else:
            right -= 1
        t = left + right
        if mx == t:
            ans.append(i + 1)
        elif mx < t:
            mx = t
            ans = [i + 1]
    return ans
"-----------------"
test()

