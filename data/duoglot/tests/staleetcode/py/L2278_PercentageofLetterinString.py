
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["foobar", "o"]
    # output: 33
    # EXPLANATION:  The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
    ,
    # example 2
    ["jjjj", "k"]
    # output: 0
    # EXPLANATION:  The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### percentageLetter 
from typing import *
def f_gold(s: str, letter: str) -> int:
    return s.count(letter) * 100 // len(s)
"-----------------"
test()

