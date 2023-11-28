
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [13, 2]
    # output: 10
    # EXPLANATION:  The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
    ,
    # example 2
    [1, 1]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findKthNumber 
from typing import *
def f_gold(n: int, k: int) -> int:
    def count(curr):
        next, cnt = curr + 1, 0
        while curr <= n:
            cnt += min(n - curr + 1, next - curr)
            next, curr = next * 10, curr * 10
        return cnt
    curr = 1
    k -= 1
    while k:
        cnt = count(curr)
        if k >= cnt:
            k -= cnt
            curr += 1
        else:
            k -= 1
            curr *= 10
    return curr
"-----------------"
test()

