
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 1, 2]]
    # output: 44
    # EXPLANATION:  The following are all the contiguous groups of wizards: - [1] from [<u><strong>1</strong></u>,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1 - [3] from [1,<u><strong>3</strong></u>,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9 - [1] from [1,3,<u><strong>1</strong></u>,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1 - [2] from [1,3,1,<u><strong>2</strong></u>] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4 - [1,3] from [<u><strong>1,3</strong></u>,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4 - [3,1] from [1,<u><strong>3,1</strong></u>,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4 - [1,2] from [1,3,<u><strong>1,2</strong></u>] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3 - [1,3,1] from [<u><strong>1,3,1</strong></u>,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5 - [3,1,2] from [1,<u><strong>3,1,2</strong></u>] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6 - [1,3,1,2] from [<u><strong>1,3,1,2</strong></u>] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7 The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.
    ,
    # example 2
    [[5, 4, 6]]
    # output: 213
    # EXPLANATION:  The following are all the contiguous groups of wizards:  - [5] from [<u><strong>5</strong></u>,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25 - [4] from [5,<u><strong>4</strong></u>,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16 - [6] from [5,4,<u><strong>6</strong></u>] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36 - [5,4] from [<u><strong>5,4</strong></u>,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36 - [4,6] from [5,<u><strong>4,6</strong></u>] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40 - [5,4,6] from [<u><strong>5,4,6</strong></u>] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60 The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### totalStrength 
from itertools import accumulate
from typing import *
def f_gold(strength: List[int]) -> int:
    n = len(strength)
    left = [-1] * n
    right = [n] * n
    stk = []
    for i, v in enumerate(strength):
        while stk and strength[stk[-1]] >= v:
            stk.pop()
        if stk:
            left[i] = stk[-1]
        stk.append(i)
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and strength[stk[-1]] > strength[i]:
            stk.pop()
        if stk:
            right[i] = stk[-1]
        stk.append(i)
    ss = list(accumulate(list(accumulate(strength, initial=0)), initial=0))
    mod = int(1e9) + 7
    ans = 0
    for i, v in enumerate(strength):
        l, r = left[i] + 1, right[i] - 1
        a = (ss[r + 2] - ss[i + 1]) * (i - l + 1)
        b = (ss[i + 1] - ss[l]) * (r - i + 1)
        ans = (ans + (a - b) * v) % mod
    return ans
"-----------------"
test()

