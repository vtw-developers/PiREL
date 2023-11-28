
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ch   ie   pr", 3]
    # output: "cipher"
    # EXPLANATION:  This is the same example described in the problem description.
    ,
    # example 2
    ["iveo    eed   l te   olc", 4]
    # output: "i love leetcode"
    # EXPLANATION:  The figure above denotes the matrix that was used to encode originalText.  The blue arrows show how we can find originalText from encodedText.
    ,
    # example 3
    ["coding", 1]
    # output: "coding"
    # EXPLANATION:  Since there is only 1 row, both originalText and encodedText are the same.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### decodeCiphertext 
from typing import *
def f_gold(encodedText: str, rows: int) -> str:
    ans = []
    cols = len(encodedText) // rows
    for j in range(cols):
        x, y = 0, j
        while x < rows and y < cols:
            ans.append(encodedText[x * cols + y])
            x, y = x + 1, y + 1
    return ''.join(ans).rstrip()
"-----------------"
test()

