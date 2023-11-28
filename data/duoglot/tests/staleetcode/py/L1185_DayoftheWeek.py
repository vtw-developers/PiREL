
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [31, 8, 2019]
    # output: "Saturday"
    ,
    # example 2
    [18, 7, 1999]
    # output: "Sunday"
    ,
    # example 3
    [15, 8, 1993]
    # output: "Sunday"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### dayOfTheWeek 
import datetime
from typing import *
def f_gold(day: int, month: int, year: int) -> str:
    return datetime.date(year, month, day).strftime('%A')
"-----------------"
test()

