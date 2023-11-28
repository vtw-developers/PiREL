
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["HOW ARE YOU"]
    # output: ["HAY","ORO","WEU"]
    # EXPLANATION: Each word is printed vertically.    "HAY"   "ORO"   "WEU"
    ,
    # example 2
    ["TO BE OR NOT TO BE"]
    # output: ["TBONTB","OEROOE","   T"]
    # EXPLANATION: Trailing spaces is not allowed.   "TBONTB"  "OEROOE"  "   T"
    ,
    # example 3
    ["CONTEST IS COMING"]
    # output: ["CIC","OSO","N M","T I","E N","S G","T"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### printVertically 
from typing import *
def f_gold(s: str) -> List[str]:
    words = s.split()
    m, n = len(words), max(len(word) for word in words)
    ans = []
    for j in range(n):
        t = []
        for i in range(m):
            word = words[i]
            t.append(word[j] if j < len(word) else ' ')
        ans.append(''.join(t).rstrip())
    return ans
"-----------------"
test()

