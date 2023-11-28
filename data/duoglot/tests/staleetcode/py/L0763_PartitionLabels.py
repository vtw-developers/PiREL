
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ababcbacadefegdehijhklij"]
    # output: [9,7,8]
    # EXPLANATION:  The partition is "ababcbaca", "defegde", "hijhklij". This is a partition so that each letter appears in at most one part. A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
    ,
    # example 2
    ["eccbbbbdec"]
    # output: [10]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### partitionLabels 
from typing import *
def f_gold(s: str) -> List[int]:
    last = [0] * 26
    for i, c in enumerate(s):
        last[ord(c) - ord('a')] = i
    ans = []
    left = right = 0
    for i, c in enumerate(s):
        right = max(right, last[ord(c) - ord('a')])
        if i == right:
            ans.append(right - left + 1)
            left = right + 1
    return ans
"-----------------"
test()

