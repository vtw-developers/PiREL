
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 100, 200, 1, 100], 1]
    # output: 100
    # EXPLANATION:  For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key. No other integers follow an occurrence of key, so we return 100.
    ,
    # example 2
    [[2, 2, 2, 2, 3], 2]
    # output: 2
    # EXPLANATION:  For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key. For target = 3, there is only one occurrence at index 4 which follows an occurrence of key. target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### mostFrequent 
from collections import Counter
from typing import *
def f_gold(nums: List[int], key: int) -> int:
    cnt = Counter()
    mx = ans = 0
    for i, v in enumerate(nums[:-1]):
        if v == key:
            target = nums[i + 1]
            cnt[target] += 1
            if mx < cnt[target]:
                mx = cnt[target]
                ans = nums[i + 1]
    return ans
"-----------------"
test()

