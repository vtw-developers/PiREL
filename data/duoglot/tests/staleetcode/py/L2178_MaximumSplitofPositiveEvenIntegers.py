
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [12]
    # output: [2,4,6]
    # EXPLANATION:  The following are valid splits: <code>(12)</code>, <code>(2 + 10)</code>, <code>(2 + 4 + 6)</code>, and <code>(4 + 8)</code>. (2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6]. Note that [2,6,4], [6,2,4], etc. are also accepted.
    ,
    # example 2
    [7]
    # output: []
    # EXPLANATION:  There are no valid splits for the given finalSum. Thus, we return an empty array.
    ,
    # example 3
    [28]
    # output: [6,8,2,12]
    # EXPLANATION:  The following are valid splits: <code>(2 + 26)</code>, <code>(6 + 8 + 2 + 12)</code>, and <code>(4 + 24)</code>.  <code>(6 + 8 + 2 + 12)</code> has the maximum number of integers, which is 4. Thus, we return [6,8,2,12]. Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumEvenSplit 
from typing import *
def f_gold(finalSum: int) -> List[int]:
    if finalSum % 2:
        return []
    i = 2
    ans = []
    while i <= finalSum:
        ans.append(i)
        finalSum -= i
        i += 2
    ans[-1] += finalSum
    return ans
"-----------------"
test()

