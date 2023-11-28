
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["AAABABB"]
    # output: true
    # EXPLANATION:  A<u>A</u>ABABB -> AABABB Alice moves first. She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.  Now it's Bob's turn. Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'. Thus, Alice wins, so return true.
    ,
    # example 2
    ["AA"]
    # output: false
    # EXPLANATION:  Alice has her turn first. There are only two 'A's and both are on the edge of the line, so she cannot move on her turn. Thus, Bob wins, so return false.
    ,
    # example 3
    ["ABBBBBBBAAA"]
    # output: false
    # EXPLANATION:  ABBBBBBBA<u>A</u>A -> ABBBBBBBAA Alice moves first. Her only option is to remove the second to last 'A' from the right.  ABBBB<u>B</u>BBAA -> ABBBBBBAA Next is Bob's turn. He has many options for which 'B' piece to remove. He can pick any.  On Alice's second turn, she has no more pieces that she can remove. Thus, Bob wins, so return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### winnerOfGame 
from typing import *
def f_gold(colors: str) -> bool:
    a = b = 0
    cnt1 = cnt2 = 0
    for c in colors:
        if c == 'A':
            a += 1
            if a > 2:
                cnt1 += 1
            b = 0
        else:
            b += 1
            if b > 2:
                cnt2 += 1
            a = 0
    return cnt1 > cnt2
"-----------------"
test()

