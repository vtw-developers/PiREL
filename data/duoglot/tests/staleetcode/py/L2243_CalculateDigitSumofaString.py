
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["11111222223", 3]
    # output: "135"
    # EXPLANATION:   - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".        Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5.    So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round. - For the second round, we divide s into "346" and "5".   Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5.    So, s becomes "13" + "5" = "135" after second round.  Now, s.length <= k, so we return "135" as the answer.
    ,
    # example 2
    ["00000000", 3]
    # output: "000"
    # EXPLANATION:   We divide s into "000", "000", and "00". Then we calculate the digit sum of each group: 0 + 0 + 0 = 0, 0 + 0 + 0 = 0, and 0 + 0 = 0.  s becomes "0" + "0" + "0" = "000", whose length is equal to k, so we return "000".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### digitSum 
from typing import *
def f_gold(s: str, k: int) -> str:
    if len(s) <= k:
        return s
    t = []
    while s:
        t.append(str(sum(int(v) for v in s[:k])))
        s = s[k:]
    return f_gold(''.join(t), k)
"-----------------"
test()

