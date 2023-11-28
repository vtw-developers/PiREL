
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]]
    # output: 2
    # EXPLANATION:   The first figure represents the dominoes as given by tops and bottoms: before we do any rotations. If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
    ,
    # example 2
    [[3, 5, 1, 2, 3], [3, 6, 3, 3, 4]]
    # output: -1
    # EXPLANATION:   In this case, it is not possible to rotate the dominoes to make one row of values equal.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minDominoRotations 
from typing import *
def f_gold(A: List[int], B: List[int]) -> int:
    a, b = A[0], B[0]
    c, d = b, a
    counta, countb = 0, 0
    countc, countd = 1, 1
    for ai, bi in zip(A[1:], B[1:]):
        if ai == a:
            pass
        elif ai != a and bi == a:
            counta += 1
        else:
            counta = -30000
        if bi == b:
            pass
        elif bi != b and ai == b:
            countb += 1
        else:
            countb = -30000
        if ai == c:
            pass
        elif ai != c and bi == c:
            countc += 1
        else:
            countc = -30000
        if bi == d:
            pass
        elif bi != d and ai == d:
            countd += 1
        else:
            countd = -30000
    if counta < 0 and countb < 0 and countc < 0 and countd < 0:
        return -1
    else:
        ans = 30000
        for count in [counta, countb, countc, countd]:
            if count >= 0:
                ans = min(ans, count)
        return ans
"-----------------"
test()

