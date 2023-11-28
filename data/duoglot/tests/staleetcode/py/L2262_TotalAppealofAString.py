
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abbca"]
    # output: 28
    # EXPLANATION:  The following are the substrings of "abbca": - Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5. - Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7. - Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7. - Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6. - Substrings of length 5: "abbca" has an appeal of 3. The sum is 3. The total sum is 5 + 7 + 7 + 6 + 3 = 28.
    ,
    # example 2
    ["code"]
    # output: 20
    # EXPLANATION:  The following are the substrings of "code": - Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4. - Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6. - Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6. - Substrings of length 4: "code" has an appeal of 4. The sum is 4. The total sum is 4 + 6 + 6 + 4 = 20.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### appealSum 
from typing import *
def f_gold(s: str) -> int:
    ans = t = 0
    pos = [-1] * 26
    for i, c in enumerate(s):
        c = ord(c) - ord('a')
        t += i - pos[c]
        ans += t
        pos[c] = i
    return ans
"-----------------"
test()

