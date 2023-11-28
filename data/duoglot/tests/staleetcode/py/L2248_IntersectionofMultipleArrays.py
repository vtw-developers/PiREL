
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]]
    # output: [3,4]
    # EXPLANATION:   The only integers present in each of nums[0] = [<u><strong>3</strong></u>,1,2,<u><strong>4</strong></u>,5], nums[1] = [1,2,<u><strong>3</strong></u>,<u><strong>4</strong></u>], and nums[2] = [<u><strong>3</strong></u>,<u><strong>4</strong></u>,5,6] are 3 and 4, so we return [3,4].
    ,
    # example 2
    [[[1, 2, 3], [4, 5, 6]]]
    # output: []
    # EXPLANATION:   There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### intersection 
from typing import *
def f_gold(nums: List[List[int]]) -> List[int]:
    cnt = [0] * 1001
    for num in nums:
        for v in num:
            cnt[v] += 1
    n = len(nums)
    return [i for i, v in enumerate(cnt) if v == n]
"-----------------"
test()

