
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]]
    # output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    ,
    # example 2
    [["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]]
    # output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findDuplicate 
from collections import defaultdict
from typing import *
def f_gold(paths: List[str]) -> List[List[str]]:
    m = defaultdict(list)
    for path in paths:
        a = path.split(" ")
        for i in range(1, len(a)):
            j = a[i].find("(")
            content = a[i][j + 1 : -1]
            name = a[0] + "/" + a[i][:j]
            m[content].append(name)
    ans = []
    for names in m.values():
        if len(names) > 1:
            ans.append(names)
    return ans
"-----------------"
test()

