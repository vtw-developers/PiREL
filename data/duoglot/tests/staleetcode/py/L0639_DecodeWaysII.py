
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["*"]
    # output: 9
    # EXPLANATION:  The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9". Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively. Hence, there are a total of 9 ways to decode "*".
    ,
    # example 2
    ["1*"]
    # output: 18
    # EXPLANATION:  The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K"). Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
    ,
    # example 3
    ["2*"]
    # output: 15
    # EXPLANATION:  The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29". "21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way. Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numDecodings 
from typing import *
def f_gold(s: str) -> int:
    mod = int(1e9 + 7)
    n = len(s)
    # dp[i - 2], dp[i - 1], dp[i]
    a, b, c = 0, 1, 0
    for i in range(1, n + 1):
        # 1 digit
        if s[i - 1] == "*":
            c = 9 * b % mod
        elif s[i - 1] != "0":
            c = b
        else:
            c = 0
        # 2 digits
        if i > 1:
            if s[i - 2] == "*" and s[i - 1] == "*":
                c = (c + 15 * a) % mod
            elif s[i - 2] == "*":
                if s[i - 1] > "6":
                    c = (c + a) % mod
                else:
                    c = (c + 2 * a) % mod
            elif s[i - 1] == "*":
                if s[i - 2] == "1":
                    c = (c + 9 * a) % mod
                elif s[i - 2] == "2":
                    c = (c + 6 * a) % mod
            elif (
                s[i - 2] != "0"
                and (ord(s[i - 2]) - ord("0")) * 10 + ord(s[i - 1]) - ord("0") <= 26
            ):
                c = (c + a) % mod
        a, b = b, c
    return c
"-----------------"
test()

