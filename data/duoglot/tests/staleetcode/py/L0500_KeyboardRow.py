
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["Hello", "Alaska", "Dad", "Peace"]]
    # output: ["Alaska","Dad"]
    ,
    # example 2
    [["omk"]]
    # output: []
    ,
    # example 3
    [["adsdf", "sfd"]]
    # output: ["adsdf","sfd"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findWords 
from typing import *
def f_gold(words: List[str]) -> List[str]:
    s1 = set('qwertyuiop')
    s2 = set('asdfghjkl')
    s3 = set('zxcvbnm')
    res = []
    for word in words:
        t = set(word.lower())
        if t <= s1 or t <= s2 or t <= s3:
            res.append(word)
    return res
"-----------------"
test()

