
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["RLRSLL"]
    # output: 5
    # EXPLANATION:  The collisions that will happen on the road are: - Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2. - Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3. - Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4. - Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5. Thus, the total number of collisions that will happen on the road is 5.
    ,
    # example 2
    ["LLRR"]
    # output: 0
    # EXPLANATION:  No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countCollisions 
from typing import *
def f_gold(directions: str) -> int:
    d = directions.lstrip('L').rstrip('R')
    return len(d) - d.count('S')
"-----------------"
test()

