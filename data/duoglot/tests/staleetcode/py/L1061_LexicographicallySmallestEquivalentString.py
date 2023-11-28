
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["parker", "morris", "parser"]
    # output: "makkek"
    # EXPLANATION:  Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i]. The characters in each group are equivalent and sorted in lexicographical order. So the answer is "makkek".
    ,
    # example 2
    ["hello", "world", "hold"]
    # output: "hdld"
    # EXPLANATION: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r]. So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
    ,
    # example 3
    ["leetcode", "programs", "sourcecode"]
    # output: "aauaaaaada"
    # EXPLANATION:  We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### smallestEquivalentString 
from typing import *
def f_gold(s1: str, s2: str, baseStr: str) -> str:
    p = list(range(26))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    for i in range(len(s1)):
        a, b = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
        pa, pb = find(a), find(b)
        if pa < pb:
            p[pb] = pa
        else:
            p[pa] = pb
    res = []
    for a in baseStr:
        a = ord(a) - ord('a')
        res.append(chr(find(a) + ord('a')))
    return ''.join(res)
"-----------------"
test()

