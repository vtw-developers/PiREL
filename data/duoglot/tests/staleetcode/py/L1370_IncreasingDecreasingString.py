
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aaaabbbbcccc"]
    # output: "abccbaabccba"
    # EXPLANATION:  After steps 1, 2 and 3 of the first iteration, result = "abc" After steps 4, 5 and 6 of the first iteration, result = "abccba" First iteration is done. Now s = "aabbcc" and we go back to step 1 After steps 1, 2 and 3 of the second iteration, result = "abccbaabc" After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
    ,
    # example 2
    ["rat"]
    # output: "art"
    # EXPLANATION:  The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortString 
from typing import *
def f_gold(s: str) -> str:
    counter = [0] * 26
    for c in s:
        counter[ord(c) - ord('a')] += 1
    ans = []
    while len(ans) < len(s):
        for i in range(26):
            if counter[i]:
                ans.append(chr(i + ord('a')))
                counter[i] -= 1
        for i in range(25, -1, -1):
            if counter[i]:
                ans.append(chr(i + ord('a')))
                counter[i] -= 1
    return ''.join(ans)
"-----------------"
test()

