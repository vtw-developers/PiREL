
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3], 3]
    # output: ["Push","Push","Pop","Push"]
    # EXPLANATION:   Read number 1 and automatically push in the array -> [1] Read number 2 and automatically push in the array then Pop it -> [1] Read number 3 and automatically push in the array -> [1,3]
    ,
    # example 2
    [[1, 2, 3], 3]
    # output: ["Push","Push","Push"]
    ,
    # example 3
    [[1, 2], 4]
    # output: ["Push","Push"]
    # EXPLANATION:  You only need to read the first 2 numbers and stop.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### buildArray 
from typing import *
def f_gold(target: List[int], n: int) -> List[str]:
    cur, ans = 1, []
    for t in target:
        for i in range(cur, n + 1):
            ans.append('Push')
            if t == i:
                cur = i + 1
                break
            ans.append('Pop')
    return ans
"-----------------"
test()

