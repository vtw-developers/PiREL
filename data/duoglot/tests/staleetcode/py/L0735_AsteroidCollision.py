
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 10, -5]]
    # output: [5,10]
    # EXPLANATION:  The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
    ,
    # example 2
    [[8, -8]]
    # output: []
    # EXPLANATION:  The 8 and -8 collide exploding each other.
    ,
    # example 3
    [[10, 2, -5]]
    # output: [10]
    # EXPLANATION:  The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### asteroidCollision 
from typing import *
def f_gold(asteroids: List[int]) -> List[int]:
    ans = []
    for a in asteroids:
        if a > 0:
            ans.append(a)
        else:
            while len(ans) > 0 and ans[-1] > 0 and ans[-1] < -a:
                ans.pop()
            if len(ans) > 0 and ans[-1] == -a:
                ans.pop()
            elif len(ans) == 0 or ans[-1] < -a:
                ans.append(a)
    return ans
"-----------------"
test()

