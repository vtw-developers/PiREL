
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["WRRBBW", "RB"]
    # output: -1
    # EXPLANATION:  It is impossible to clear all the balls. The best you can do is: - Insert 'R' so the board becomes WRR<u>R</u>BBW. W<u>RRR</u>BBW -> WBBW. - Insert 'B' so the board becomes WBB<u>B</u>W. W<u>BBB</u>W -> WW. There are still balls remaining on the board, and you are out of balls to insert.
    ,
    # example 2
    ["WWRRBBWW", "WRBRW"]
    # output: 2
    # EXPLANATION:  To make the board empty: - Insert 'R' so the board becomes WWRR<u>R</u>BBWW. WW<u>RRR</u>BBWW -> WWBBWW. - Insert 'B' so the board becomes WWBB<u>B</u>WW. WW<u>BBB</u>WW -> <u>WWWW</u> -> empty. 2 balls from your hand were needed to clear the board.
    ,
    # example 3
    ["G", "GGGGG"]
    # output: 2
    # EXPLANATION:  To make the board empty: - Insert 'G' so the board becomes G<u>G</u>. - Insert 'G' so the board becomes GG<u>G</u>. <u>GGG</u> -> empty. 2 balls from your hand were needed to clear the board.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMinStep 
import re
from collections import deque
from typing import *
def f_gold(board: str, hand: str) -> int:
    def remove(s):
        while len(s):
            next = re.sub(r'B{3,}|G{3,}|R{3,}|W{3,}|Y{3,}', '', s)
            if len(next) == len(s):
                break
            s = next
        return s
    visited = set()
    q = deque([(board, hand)])
    while q:
        state, balls = q.popleft()
        if not state:
            return len(hand) - len(balls)
        for ball in set(balls):
            b = balls.replace(ball, '', 1)
            for i in range(1, len(state) + 1):
                s = state[:i] + ball + state[i:]
                s = remove(s)
                if s not in visited:
                    visited.add(s)
                    q.append((s, b))
    return -1
"-----------------"
test()

