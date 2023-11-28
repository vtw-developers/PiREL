
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abc"]
    # output: 5
    # EXPLANATION: The characters are printed as follows: - Type the character 'a' in 1 second since the pointer is initially on 'a'. - Move the pointer clockwise to 'b' in 1 second. - Type the character 'b' in 1 second. - Move the pointer clockwise to 'c' in 1 second. - Type the character 'c' in 1 second.
    ,
    # example 2
    ["bza"]
    # output: 7
    # EXPLANATION: The characters are printed as follows: - Move the pointer clockwise to 'b' in 1 second. - Type the character 'b' in 1 second. - Move the pointer counterclockwise to 'z' in 2 seconds. - Type the character 'z' in 1 second. - Move the pointer clockwise to 'a' in 1 second. - Type the character 'a' in 1 second.
    ,
    # example 3
    ["zjpc"]
    # output: 34
    # EXPLANATION:  The characters are printed as follows: - Move the pointer counterclockwise to 'z' in 1 second. - Type the character 'z' in 1 second. - Move the pointer clockwise to 'j' in 10 seconds. - Type the character 'j' in 1 second. - Move the pointer clockwise to 'p' in 6 seconds. - Type the character 'p' in 1 second. - Move the pointer counterclockwise to 'c' in 13 seconds. - Type the character 'c' in 1 second.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minTimeToType 
from typing import *
def f_gold(word: str) -> int:
    ans = prev = 0
    for c in word:
        curr = ord(c) - ord('a')
        t = abs(prev - curr)
        t = min(t, 26 - t)
        ans += t + 1
        prev = curr
    return ans
"-----------------"
test()

