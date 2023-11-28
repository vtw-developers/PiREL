
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["GGLLGG"]
    # output: true
    # EXPLANATION:  The robot is initially at (0, 0) facing the north direction. "G": move one step. Position: (0, 1). Direction: North. "G": move one step. Position: (0, 2). Direction: North. "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West. "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South. "G": move one step. Position: (0, 1). Direction: South. "G": move one step. Position: (0, 0). Direction: South. Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0). Based on that, we return true.
    ,
    # example 2
    ["GG"]
    # output: false
    # EXPLANATION:  The robot is initially at (0, 0) facing the north direction. "G": move one step. Position: (0, 1). Direction: North. "G": move one step. Position: (0, 2). Direction: North. Repeating the instructions, keeps advancing in the north direction and does not go into cycles. Based on that, we return false.
    ,
    # example 3
    ["GL"]
    # output: true
    # EXPLANATION:  The robot is initially at (0, 0) facing the north direction. "G": move one step. Position: (0, 1). Direction: North. "L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West. "G": move one step. Position: (-1, 1). Direction: West. "L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South. "G": move one step. Position: (-1, 0). Direction: South. "L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East. "G": move one step. Position: (0, 0). Direction: East. "L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North. Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0). Based on that, we return true.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isRobotBounded 
from typing import *
def f_gold(instructions: str) -> bool:
    cur, direction = 0, [0] * 4
    for ins in instructions:
        if ins == 'L':
            cur = (cur + 1) % 4
        elif ins == 'R':
            cur = (cur + 3) % 4
        else:
            direction[cur] += 1
    return cur != 0 or (
        direction[0] == direction[2] and direction[1] == direction[3]
    )
"-----------------"
test()

