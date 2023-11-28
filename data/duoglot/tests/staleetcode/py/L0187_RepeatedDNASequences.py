
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"]
    # output: ["AAAAACCCCC","CCCCCAAAAA"]
    ,
    # example 2
    ["AAAAAAAAAAAAA"]
    # output: ["AAAAAAAAAA"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findRepeatedDnaSequences 
from collections import Counter
from typing import *
def f_gold(s: str) -> List[str]:
    n = len(s) - 10
    cnt = Counter()
    ans = []
    for i in range(n + 1):
        sub = s[i : i + 10]
        cnt[sub] += 1
        if cnt[sub] == 2:
            ans.append(sub)
    return ans
"-----------------"
test()

