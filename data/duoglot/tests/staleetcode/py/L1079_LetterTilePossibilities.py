
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["AAB"]
    # output: 8
    # EXPLANATION: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
    ,
    # example 2
    ["AAABBC"]
    # output: 188
    ,
    # example 3
    ["V"]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numTilePossibilities 
from typing import *
def f_gold(tiles: str) -> int:
    def dfs():
        ans = 0
        for i in range(26):
            if cnt[i]:
                ans += 1
                cnt[i] -= 1
                ans += dfs()
                cnt[i] += 1
        return ans
    cnt = [0] * 26
    for t in tiles:
        cnt[ord(t) - ord('A')] += 1
    return dfs()
"-----------------"
test()

