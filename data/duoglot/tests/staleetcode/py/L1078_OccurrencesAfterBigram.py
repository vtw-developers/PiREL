
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["alice is a good girl she is a good student", "a", "good"]
    # output: ["girl","student"]
    ,
    # example 2
    ["we will we will rock you", "we", "will"]
    # output: ["we","rock"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findOcurrences 
from typing import *
def f_gold(text: str, first: str, second: str) -> List[str]:
    words = text.split(' ')
    return [
        words[i + 2]
        for i in range(len(words) - 2)
        if words[i] == first and words[i + 1] == second
    ]
"-----------------"
test()

