
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["owoztneoer"]
    # output: "012"
    ,
    # example 2
    ["fviefuro"]
    # output: "45"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### originalDigits 
from collections import Counter
from typing import *
def f_gold(s: str) -> str:
    counter = Counter(s)
    cnt = [0] * 10
    cnt[0] = counter['z']
    cnt[2] = counter['w']
    cnt[4] = counter['u']
    cnt[6] = counter['x']
    cnt[8] = counter['g']
    cnt[3] = counter['h'] - cnt[8]
    cnt[5] = counter['f'] - cnt[4]
    cnt[7] = counter['s'] - cnt[6]
    cnt[1] = counter['o'] - cnt[0] - cnt[2] - cnt[4]
    cnt[9] = counter['i'] - cnt[5] - cnt[6] - cnt[8]
    return ''.join(cnt[i] * str(i) for i in range(10))
"-----------------"
test()

