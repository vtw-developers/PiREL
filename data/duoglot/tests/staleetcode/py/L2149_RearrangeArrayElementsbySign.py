
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, -2, -5, 2, -4]]
    # output: [3,-2,1,-5,2,-4]
    # EXPLANATION:  The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4]. The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4]. Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.
    ,
    # example 2
    [[-1, 1]]
    # output: [1,-1]
    # EXPLANATION:  1 is the only positive integer and -1 the only negative integer in nums. So nums is rearranged to [1,-1].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rearrangeArray 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    i, j = 0, 1
    for num in nums:
        if num > 0:
            ans[i] = num
            i += 2
        else:
            ans[j] = num
            j += 2
    return ans
"-----------------"
test()

