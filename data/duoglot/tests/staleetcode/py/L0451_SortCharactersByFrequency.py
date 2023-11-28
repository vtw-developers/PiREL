
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["tree"]
    # output: "eert"
    # EXPLANATION:  'e' appears twice while 'r' and 't' both appear once. So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
    ,
    # example 2
    ["cccaaa"]
    # output: "aaaccc"
    # EXPLANATION:  Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers. Note that "cacaca" is incorrect, as the same characters must be together.
    ,
    # example 3
    ["Aabb"]
    # output: "bbAa"
    # EXPLANATION:  "bbaA" is also a valid answer, but "Aabb" is incorrect. Note that 'A' and 'a' are treated as two different characters.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### frequencySort 
from collections import defaultdict
from collections import Counter
from typing import *
def f_gold(s: str) -> str:
    counter = Counter(s)
    buckets = defaultdict(list)
    for c, freq in counter.items():
        buckets[freq].append(c)
    res = []
    for i in range(len(s), -1, -1):
        if buckets[i]:
            for c in buckets[i]:
                res.append(c * i)
    return ''.join(res)
"-----------------"
test()

