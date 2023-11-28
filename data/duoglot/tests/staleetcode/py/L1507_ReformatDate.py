
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["20th Oct 2052"]
    # output: "2052-10-20"
    ,
    # example 2
    ["6th Jun 1933"]
    # output: "1933-06-06"
    ,
    # example 3
    ["26th May 1960"]
    # output: "1960-05-26"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reformatDate 
from typing import *
def f_gold(date: str) -> str:
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    mapper = {v: str(k + 1) for k, v in enumerate(months)}
    split = date.split(' ')
    year = split[2]
    month = mapper.get(split[1])
    day = split[0][: len(split[0]) - 2]
    return year + '-' + month.zfill(2) + '-' + day.zfill(2)
"-----------------"
test()

