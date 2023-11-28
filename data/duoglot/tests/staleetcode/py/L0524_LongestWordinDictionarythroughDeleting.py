
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abpcplea", ["ale", "apple", "monkey", "plea"]]
    # output: "apple"
    ,
    # example 2
    ["abpcplea", ["a", "b", "c"]]
    # output: "a"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findLongestWord 
from typing import *
def f_gold(s: str, dictionary: List[str]) -> str:
    def check(a, b):
        m, n = len(a), len(b)
        i = j = 0
        while i < m and j < n:
            if a[i] == b[j]:
                j += 1
            i += 1
        return j == n
    ans = ''
    for a in dictionary:
        if check(s, a) and (len(ans) < len(a) or (len(ans) == len(a) and ans > a)):
            ans = a
    return ans
"-----------------"
test()

