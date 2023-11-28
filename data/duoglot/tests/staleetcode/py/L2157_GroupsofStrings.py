
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a", "b", "ab", "cde"]]
    # output: [2,3]
    # EXPLANATION:  - words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2]. - words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2]. - words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1]. - words[3] is not connected to any string in words. Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.
    ,
    # example 2
    [["a", "ab", "abc"]]
    # output: [1,3]
    # EXPLANATION:  - words[0] is connected to words[1]. - words[1] is connected to words[0] and words[2]. - words[2] is connected to words[1]. Since all strings are connected to each other, they should be grouped together. Thus, the size of the largest group is 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### groupStrings 
from collections import Counter
from typing import *
def f_gold(words: List[str]) -> List[int]:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(a, b):
        nonlocal mx, n
        if b not in p:
            return
        pa, pb = find(a), find(b)
        if pa == pb:
            return
        p[pa] = pb
        size[pb] += size[pa]
        mx = max(mx, size[pb])
        n -= 1
    p = {}
    size = Counter()
    n = len(words)
    mx = 0
    for word in words:
        x = 0
        for c in word:
            x |= 1 << (ord(c) - ord('a'))
        p[x] = x
        size[x] += 1
        mx = max(mx, size[x])
        if size[x] > 1:
            n -= 1
    for x in p.keys():
        for i in range(26):
            union(x, x ^ (1 << i))
            if (x >> i) & 1:
                for j in range(26):
                    if ((x >> j) & 1) == 0:
                        union(x, x ^ (1 << i) | (1 << j))
    return [n, mx]
"-----------------"
test()

