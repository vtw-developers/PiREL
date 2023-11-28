
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7, 4]
    # output: [1,2,3,1]
    # EXPLANATION:  On the first turn, ans[0] += 1, and the array is [1,0,0,0]. On the second turn, ans[1] += 2, and the array is [1,2,0,0]. On the third turn, ans[2] += 3, and the array is [1,2,3,0]. On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
    ,
    # example 2
    [10, 3]
    # output: [5,2,3]
    # EXPLANATION:  On the first turn, ans[0] += 1, and the array is [1,0,0]. On the second turn, ans[1] += 2, and the array is [1,2,0]. On the third turn, ans[2] += 3, and the array is [1,2,3]. On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### distributeCandies 
from typing import *
def f_gold(candies: int, num_people: int) -> List[int]:
    ans = [0] * num_people
    i = 0
    while candies > 0:
        ans[i % num_people] += min(candies, i + 1)
        candies -= min(candies, i + 1)
        i += 1
    return ans
"-----------------"
test()

