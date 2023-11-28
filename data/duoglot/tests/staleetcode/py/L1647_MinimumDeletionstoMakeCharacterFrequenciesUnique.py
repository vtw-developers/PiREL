
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aab"]
    # output: 0
    # EXPLANATION:  <code>s</code> is already good.
    ,
    # example 2
    ["aaabbbcc"]
    # output: 2
    # EXPLANATION:  You can delete two 'b's resulting in the good string "aaabcc". Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
    ,
    # example 3
    ["ceabaacb"]
    # output: 2
    # EXPLANATION:  You can delete both 'c's resulting in the good string "eabaab". Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minDeletions 
from collections import Counter
from typing import *
def f_gold(s: str) -> int:
    counter = Counter(s)
    vals = [v for v in counter.values()]
    vals.sort(reverse=True)
    ans = 0
    for i in range(1, len(vals)):
        while vals[i] >= vals[i - 1] and vals[i] > 0:
            vals[i] -= 1
            ans += 1
    return ans
"-----------------"
test()

