
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["19:34"]
    # output: "19:39"
    # EXPLANATION:  The next closest time choosing from digits <strong>1</strong>, <strong>9</strong>, <strong>3</strong>, <strong>4</strong>, is <strong>19:39</strong>, which occurs 5 minutes later. It is not <strong>19:33</strong>, because this occurs 23 hours and 59 minutes later.
    ,
    # example 2
    ["23:59"]
    # output: "22:22"
    # EXPLANATION:  The next closest time choosing from digits <strong>2</strong>, <strong>3</strong>, <strong>5</strong>, <strong>9</strong>, is <strong>22:22</strong>. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### nextClosestTime 
import math
from math import inf
from typing import *
def f_gold(time: str) -> str:
    def check(t):
        h, m = int(t[:2]), int(t[2:])
        return 0 <= h < 24 and 0 <= m < 60
    def dfs(curr):
        if len(curr) == 4:
            if not check(curr):
                return
            nonlocal ans, d
            p = int(curr[:2]) * 60 + int(curr[2:])
            if t < p < t + d:
                d = p - t
                ans = curr[:2] + ':' + curr[2:]
            return
        for c in s:
            dfs(curr + c)
    s = {c for c in time if c != ':'}
    t = int(time[:2]) * 60 + int(time[3:])
    d = float('inf')
    ans = None
    dfs('')
    if ans is None:
        mi = min(int(c) for c in s)
        ans = f'{mi}{mi}:{mi}{mi}'
    return ans
"-----------------"
test()

