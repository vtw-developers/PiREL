
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0]]
    # output: 16
    # EXPLANATION:  You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2. Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2. In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed. Total number of candies collected = 7 + 4 + 5 = 16 candy.
    ,
    # example 2
    [[1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [[1, 2, 3, 4, 5], [], [], [], [], []], [[1, 2, 3, 4, 5], [], [], [], [], []], [0]]
    # output: 6
    # EXPLANATION:  You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys. The total number of candies will be 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxCandies 
from collections import deque
from typing import *
def f_gold(status: List[int],
    candies: List[int],
    keys: List[List[int]],
    containedBoxes: List[List[int]],
    initialBoxes: List[int],
) -> int:
    q = deque([i for i in initialBoxes if status[i] == 1])
    ans = sum(candies[i] for i in initialBoxes if status[i] == 1)
    has = set(initialBoxes)
    took = {i for i in initialBoxes if status[i] == 1}
    while q:
        i = q.popleft()
        for k in keys[i]:
            status[k] = 1
            if k in has and k not in took:
                ans += candies[k]
                took.add(k)
                q.append(k)
        for j in containedBoxes[i]:
            has.add(j)
            if status[j] and j not in took:
                ans += candies[j]
                took.add(j)
                q.append(j)
    return ans
"-----------------"
test()

