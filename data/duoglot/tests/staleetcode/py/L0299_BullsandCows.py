
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1807", "7810"]
    # output: "1A3B"
    # EXPLANATION:  Bulls are connected with a '|' and cows are underlined: "1807"   | "<u>7</u>8<u>10</u>"
    ,
    # example 2
    ["1123", "0111"]
    # output: "1A1B"
    # EXPLANATION:  Bulls are connected with a '|' and cows are underlined: "1123"        "1123"   |      or     | "01<u>1</u>1"        "011<u>1</u>" Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getHint 
from typing import *
def f_gold(secret: str, guess: str) -> str:
    x = y = 0
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            x += 1
        else:
            cnt1[int(secret[i])] += 1
            cnt2[int(guess[i])] += 1
    for i in range(10):
        y += min(cnt1[i], cnt2[i])
    return f'{x}A{y}B'
"-----------------"
test()

