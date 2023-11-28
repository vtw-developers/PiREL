
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 6, 5, 8]]
    # output: [10,8]
    # EXPLANATION:   - 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums. - 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums. - 5 is not a lonely number since 6 appears in nums and vice versa. Hence, the lonely numbers in nums are [10, 8]. Note that [8, 10] may also be returned.
    ,
    # example 2
    [[1, 3, 5, 3]]
    # output: [1,5]
    # EXPLANATION:   - 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums. - 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums. - 3 is not a lonely number since it appears twice. Hence, the lonely numbers in nums are [1, 5]. Note that [5, 1] may also be returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findLonely 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    counter = Counter(nums)
    ans = []
    for num, cnt in counter.items():
        if cnt == 1 and counter[num - 1] == 0 and counter[num + 1] == 0:
            ans.append(num)
    return ans
"-----------------"
test()

