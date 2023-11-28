
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3], 1]
    # output: [1,0,2,1]
    # EXPLANATION:  If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
    ,
    # example 2
    [[6, 2, 7, 3], 4]
    # output: [4,2,0,7,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### decode 
from typing import *
def f_gold(encoded: List[int], first: int) -> List[int]:
    ans = [first]
    for e in encoded:
        ans.append(ans[-1] ^ e)
    return ans
"-----------------"
test()

