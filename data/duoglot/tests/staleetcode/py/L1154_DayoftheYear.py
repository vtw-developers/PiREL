
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["2019-01-09"]
    # output: 9
    # EXPLANATION:  Given date is the 9th day of the year in 2019.
    ,
    # example 2
    ["2019-02-10"]
    # output: 41
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### dayOfYear 
from typing import *
def f_gold(date: str) -> int:
    year, month, day = (int(e) for e in date.split('-'))
    d = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
    days = [31, d, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days[: month - 1]) + day
"-----------------"
test()

