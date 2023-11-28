
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["0"]
    # output: true
    ,
    # example 2
    ["e"]
    # output: false
    ,
    # example 3
    ["."]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isNumber 
import re
from typing import *
def f_gold(s):
    """
    :type s: str
    :rtype: bool
    """
    NumberRE = "[\+\-]?((\d+\.?\d*|\d*\.?\d+)(e[\+\-]?\d+)?)"
    s = s.strip()
    Ans = re.match(NumberRE, s)
    if Ans and len(s) == Ans.regs[0][1]:
        return True
    return False
"-----------------"
test()

