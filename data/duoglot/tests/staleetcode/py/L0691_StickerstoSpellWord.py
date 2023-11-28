
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["with", "example", "science"], "thehat"]
    # output: 3
    # EXPLANATION:  We can use 2 "with" stickers, and 1 "example" sticker. After cutting and rearrange the letters of those stickers, we can form the target "thehat". Also, this is the minimum number of stickers necessary to form the target string.
    ,
    # example 2
    [["notice", "possible"], "basicbasic"]
    # output: -1
    # EXPLANATION:  We cannot form the target "basicbasic" from cutting letters from the given stickers.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minStickers 
from collections import deque
from collections import Counter
from typing import *
def f_gold(stickers: List[str], target: str) -> int:
    q = deque([0])
    ans = 0
    n = len(target)
    vis = [False] * (1 << n)
    vis[0] = True
    while q:
        for _ in range(len(q)):
            state = q.popleft()
            if state == (1 << n) - 1:
                return ans
            for s in stickers:
                nxt = state
                cnt = Counter(s)
                for i, c in enumerate(target):
                    if not (nxt & (1 << i)) and cnt[c]:
                        nxt |= 1 << i
                        cnt[c] -= 1
                if not vis[nxt]:
                    vis[nxt] = True
                    q.append(nxt)
        ans += 1
    return -1
"-----------------"
test()

