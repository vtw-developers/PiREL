
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [240, 2]
    # output: 2
    # EXPLANATION:  The following are the substrings of num of length k: - "24" from "<strong><u>24</u></strong>0": 24 is a divisor of 240. - "40" from "2<u><strong>40</strong></u>": 40 is a divisor of 240. Therefore, the k-beauty is 2.
    ,
    # example 2
    [430043, 2]
    # output: 2
    # EXPLANATION:  The following are the substrings of num of length k: - "43" from "<u><strong>43</strong></u>0043": 43 is a divisor of 430043. - "30" from "4<u><strong>30</strong></u>043": 30 is not a divisor of 430043. - "00" from "43<u><strong>00</strong></u>43": 0 is not a divisor of 430043. - "04" from "430<u><strong>04</strong></u>3": 4 is not a divisor of 430043. - "43" from "4300<u><strong>43</strong></u>": 43 is a divisor of 430043. Therefore, the k-beauty is 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### divisorSubstrings 
from typing import *
def f_gold(num: int, k: int) -> int:
    cnt = 0
    s = str(num)
    for i in range(len(s) - k + 1):
        tmp = int(s[i : i + k])
        if tmp != 0 and num % tmp == 0:
            cnt += 1
    return cnt
"-----------------"
test()

