
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 7], 3]
    # output: 3
    # EXPLANATION:  Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
    ,
    # example 2
    [[5, 4, 3, 2, 1, 1000000000], 2]
    # output: 999999999
    # EXPLANATION:  We can use baskets 1 and 1000000000.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxDistance 
from typing import *
def f_gold(position: List[int], m: int) -> int:
    def check(f):
        prev = position[0]
        cnt = 1
        for curr in position[1:]:
            if curr - prev >= f:
                prev = curr
                cnt += 1
        return cnt >= m
    position.sort()
    left, right = 1, position[-1]
    while left < right:
        mid = (left + right + 1) >> 1
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left
"-----------------"
test()

