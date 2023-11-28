
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["23"]
    # output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    ,
    # example 2
    [""]
    # output: []
    ,
    # example 3
    ["2"]
    # output: ["a","b","c"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### letterCombinations 
from typing import *
def f_gold(digits: str) -> List[str]:
    n = len(digits)
    if n == 0:
        return []
    chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    strs = [chars[int(d) - 2] for d in digits]
    res = []
    for s in strs:
        if not res:
            res = list(s)
        else:
            cache = []
            for item in res:
                for letter in s:
                    cache.append(item + letter)
            res = cache
    return res
"-----------------"
test()

