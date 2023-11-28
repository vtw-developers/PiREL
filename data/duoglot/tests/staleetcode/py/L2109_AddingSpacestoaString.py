
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["LeetcodeHelpsMeLearn", [8, 13, 15]]
    # output: "Leetcode Helps Me Learn"
    # EXPLANATION:   The indices 8, 13, and 15 correspond to the underlined characters in "Leetcode<u><strong>H</strong></u>elps<u><strong>M</strong></u>e<u><strong>L</strong></u>earn". We then place spaces before those characters.
    ,
    # example 2
    ["icodeinpython", [1, 5, 7, 9]]
    # output: "i code in py thon"
    # EXPLANATION:  The indices 1, 5, 7, and 9 correspond to the underlined characters in "i<u><strong>c</strong></u>ode<u><strong>i</strong></u>n<u><strong>p</strong></u>y<u><strong>t</strong></u>hon". We then place spaces before those characters.
    ,
    # example 3
    ["spacing", [0, 1, 2, 3, 4, 5, 6]]
    # output: " s p a c i n g"
    # EXPLANATION:  We are also able to place spaces before the first character of the string.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### addSpaces 
from typing import *
def f_gold(s: str, spaces: List[int]) -> str:
    ans = []
    j = 0
    for i, c in enumerate(s):
        if j < len(spaces) and i == spaces[j]:
            ans.append(' ')
            j += 1
        ans.append(c)
    return ''.join(ans)
"-----------------"
test()

