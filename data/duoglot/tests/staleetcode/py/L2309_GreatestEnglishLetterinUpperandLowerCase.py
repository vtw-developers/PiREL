
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["lEeTcOdE"]
    # output: "E"
    # EXPLANATION:  The letter 'E' is the only letter to appear in both lower and upper case.
    ,
    # example 2
    ["arRAzFif"]
    # output: "R"
    # EXPLANATION:  The letter 'R' is the greatest letter to appear in both lower and upper case. Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
    ,
    # example 3
    ["AbCdEfGhIjK"]
    # output: ""
    # EXPLANATION:  There is no letter that appears in both lower and upper case.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### greatestLetter 
from string import ascii_uppercase
from typing import *
def f_gold(s: str) -> str:
    ss = set(s)
    for c in ascii_uppercase[::-1]:
        if c in ss and c.lower() in ss:
            return c
    return ''
"-----------------"
test()

