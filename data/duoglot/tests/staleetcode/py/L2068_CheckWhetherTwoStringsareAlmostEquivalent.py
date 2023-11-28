
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aaaa", "bccb"]
    # output: false
    # EXPLANATION:  There are 4 'a's in "aaaa" but 0 'a's in "bccb". The difference is 4, which is more than the allowed 3.
    ,
    # example 2
    ["abcdeef", "abaaacc"]
    # output: true
    # EXPLANATION:  The differences between the frequencies of each letter in word1 and word2 are at most 3: - 'a' appears 1 time in word1 and 4 times in word2. The difference is 3. - 'b' appears 1 time in word1 and 1 time in word2. The difference is 0. - 'c' appears 1 time in word1 and 2 times in word2. The difference is 1. - 'd' appears 1 time in word1 and 0 times in word2. The difference is 1. - 'e' appears 2 times in word1 and 0 times in word2. The difference is 2. - 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.
    ,
    # example 3
    ["cccddabba", "babababab"]
    # output: true
    # EXPLANATION:  The differences between the frequencies of each letter in word1 and word2 are at most 3: - 'a' appears 2 times in word1 and 4 times in word2. The difference is 2. - 'b' appears 2 times in word1 and 5 times in word2. The difference is 3. - 'c' appears 3 times in word1 and 0 times in word2. The difference is 3. - 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkAlmostEquivalent 
from collections import defaultdict
from typing import *
def f_gold(word1: str, word2: str) -> bool:
    counter = defaultdict(int)
    for c in word1:
        counter[c] += 1
    for c in word2:
        counter[c] -= 1
    return all(abs(x) <= 3 for x in counter.values())
"-----------------"
test()

