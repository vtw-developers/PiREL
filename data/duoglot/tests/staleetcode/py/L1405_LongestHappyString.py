
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 1, 7]
    # output: "ccaccbcc"
    # EXPLANATION:  "ccbccacc" would also be a correct answer.
    ,
    # example 2
    [7, 1, 0]
    # output: "aabaa"
    # EXPLANATION:  It is the only correct answer in this case.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestDiverseString 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(a: int, b: int, c: int) -> str:
    h = []
    if a > 0:
        heappush(h, [-a, 'a'])
    if b > 0:
        heappush(h, [-b, 'b'])
    if c > 0:
        heappush(h, [-c, 'c'])
    ans = []
    while len(h) > 0:
        cur = heappop(h)
        if len(ans) >= 2 and ans[-1] == cur[1] and ans[-2] == cur[1]:
            if len(h) == 0:
                break
            nxt = heappop(h)
            ans.append(nxt[1])
            if -nxt[0] > 1:
                nxt[0] += 1
                heappush(h, nxt)
            heappush(h, cur)
        else:
            ans.append(cur[1])
            if -cur[0] > 1:
                cur[0] += 1
                heappush(h, cur)
    return ''.join(ans)
"-----------------"
test()

