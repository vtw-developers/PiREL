
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1000, 100, 10, 2]]
    # output: "1000/(100/10/2)"
    # EXPLANATION:  1000/(100/10/2) = 1000/((100/10)/2) = 200 However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since they don't influence the operation priority. So you should return "1000/(100/10/2)". Other cases: 1000/(100/10)/2 = 50 1000/(100/(10/2)) = 50 1000/100/10/2 = 0.5 1000/100/(10/2) = 2
    ,
    # example 2
    [[2, 3, 4]]
    # output: "2/(3/4)"
    ,
    # example 3
    [[2]]
    # output: "2"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### optimalDivision 
from typing import *
def f_gold(nums: List[int]) -> str:
    n = len(nums)
    if n == 1:
        return str(nums[0])
    if n == 2:
        return f'{nums[0]}/{nums[1]}'
    return f'{nums[0]}/({"/".join(map(str, nums[1:]))})'
"-----------------"
test()

