
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["dfa12321afd"]
    # output: 2
    # EXPLANATION:  The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
    ,
    # example 2
    ["abc1111"]
    # output: -1
    # EXPLANATION:  The digits that appear in s are [1]. There is no second largest digit.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### secondHighest 
from typing import *
def f_gold(s: str) -> int:
    largest_digit = second_largest_digit = -1
    for c in s:
        if c.isdigit():
            num = int(c)
            if num > largest_digit:
                second_largest_digit, largest_digit = largest_digit, num
            elif num > second_largest_digit and num < largest_digit:
                second_largest_digit = num
    return second_largest_digit
"-----------------"
test()

