
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["eat", "tea", "tan", "ate", "nat", "bat"]]
    # output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    ,
    # example 2
    [[""]]
    # output: [[""]]
    ,
    # example 3
    [["a"]]
    # output: [["a"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### groupAnagrams 
from collections import defaultdict
from typing import *
def f_gold(strs: List[str]) -> List[List[str]]:
    chars = defaultdict(list)
    for s in strs:
        k = ''.join(sorted(list(s)))
        chars[k].append(s)
    return list(chars.values())
"-----------------"
test()

