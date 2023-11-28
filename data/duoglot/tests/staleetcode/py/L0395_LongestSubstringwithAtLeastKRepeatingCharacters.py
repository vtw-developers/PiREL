
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aaabb", 3]
    # output: 3
    # EXPLANATION:  The longest substring is "aaa", as 'a' is repeated 3 times.
    ,
    # example 2
    ["ababbc", 2]
    # output: 5
    # EXPLANATION:  The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestSubstring 
from typing import *
def f_gold(s: str, k: int) -> int:
    n = len(s)
    maxLength = 0
    for i in range(1, 27):
        counter = dict()
        left = 0
        right = 0
        unique = 0
        kCount = 0
        while right < n:
            if unique <= i:
                r = s[right]
                counter[r] = counter.get(r, 0) + 1
                if counter[r] == 1:
                    unique += 1
                if counter[r] == k:
                    kCount += 1
                right += 1
            else:
                l = s[left]
                counter[l] = counter.get(l, 0) - 1
                if counter[l] == 0:
                    unique -= 1
                if counter[l] == k - 1:
                    kCount -= 1
                left += 1
            if unique == i and kCount == i:
                maxLength = max(maxLength, right - left)
    return maxLength
"-----------------"
test()

