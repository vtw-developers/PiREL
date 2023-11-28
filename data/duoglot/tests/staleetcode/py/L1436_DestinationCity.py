
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]]
    # output: "Sao Paulo"
    # EXPLANATION:  Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
    ,
    # example 2
    [[["B", "C"], ["D", "B"], ["C", "A"]]]
    # output: "A"
    # EXPLANATION:  All possible trips are:  "D" -> "B" -> "C" -> "A".  "B" -> "C" -> "A".  "C" -> "A".  "A".  Clearly the destination city is "A".
    ,
    # example 3
    [[["A", "Z"]]]
    # output: "Z"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### destCity 
from typing import *
def f_gold(paths: List[List[str]]) -> str:
    mp = {a: b for a, b in paths}
    a = paths[0][0]
    while mp.get(a):
        a = mp[a]
    return a
"-----------------"
test()

