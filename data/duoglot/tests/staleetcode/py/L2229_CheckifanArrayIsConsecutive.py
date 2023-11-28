
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 4, 2]]
    # output: true
    # EXPLANATION:  The minimum value is 1 and the length of nums is 4. All of the values in the range [x, x + n - 1] = [1, 1 + 4 - 1] = [1, 4] = (1, 2, 3, 4) occur in nums. Therefore, nums is consecutive.
    ,
    # example 2
    [[1, 3]]
    # output: false
    # EXPLANATION:  The minimum value is 1 and the length of nums is 2. The value 2 in the range [x, x + n - 1] = [1, 1 + 2 - 1], = [1, 2] = (1, 2) does not occur in nums. Therefore, nums is not consecutive.
    ,
    # example 3
    [[3, 5, 4]]
    # output: true
    # EXPLANATION:  The minimum value is 3 and the length of nums is 3. All of the values in the range [x, x + n - 1] = [3, 3 + 3 - 1] = [3, 5] = (3, 4, 5) occur in nums. Therefore, nums is consecutive.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isConsecutive 
from typing import *
def f_gold(nums: List[int]) -> bool:
    mi, mx = min(nums), max(nums)
    n = len(nums)
    return len(set(nums)) == n and mx == mi + n - 1
"-----------------"
test()

