
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["][]["]
    # output: 1
    # EXPLANATION:  You can make the string balanced by swapping index 0 with index 3. The resulting string is "[[]]".
    ,
    # example 2
    ["]]][[["]
    # output: 2
    # EXPLANATION:  You can do the following to make the string balanced: - Swap index 0 with index 4. s = "[]][][". - Swap index 1 with index 5. s = "[[][]]". The resulting string is "[[][]]".
    ,
    # example 3
    ["[]"]
    # output: 0
    # EXPLANATION:  The string is already balanced.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSwaps 
from typing import *
def f_gold(s: str) -> int:
    ans = 0
    for c in s:
        if c == '[':
            ans += 1
        elif ans:
            ans -= 1
    return (ans + 1) >> 1
"-----------------"
test()

