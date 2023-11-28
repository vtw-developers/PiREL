
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["0201", "0101", "0102", "1212", "2002"], "0202"]
    # output: 6
    # EXPLANATION:   A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202". Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid, because the wheels of the lock become stuck after the display becomes the dead end "0102".
    ,
    # example 2
    [["8888"], "0009"]
    # output: 1
    # EXPLANATION:  We can turn the last wheel in reverse to move from "0000" -> "0009".
    ,
    # example 3
    [["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"]
    # output: -1
    # EXPLANATION:  We cannot reach the target without getting stuck.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### openLock 
from collections import deque
from typing import *
def f_gold(deadends: List[str], target: str) -> int:
    def next(s):
        res = []
        s = list(s)
        for i in range(4):
            c = s[i]
            s[i] = '9' if c == '0' else str(int(c) - 1)
            res.append(''.join(s))
            s[i] = '0' if c == '9' else str(int(c) + 1)
            res.append(''.join(s))
            s[i] = c
        return res
    def extend(m1, m2, q):
        for _ in range(len(q)):
            p = q.popleft()
            step = m1[p]
            for t in next(p):
                if t in s or t in m1:
                    continue
                if t in m2:
                    return step + 1 + m2[t]
                m1[t] = step + 1
                q.append(t)
        return -1
    def bfs():
        m1, m2 = {"0000": 0}, {target: 0}
        q1, q2 = deque([('0000')]), deque([(target)])
        while q1 and q2:
            t = extend(m1, m2, q1) if len(q1) <= len(q2) else extend(m2, m1, q2)
            if t != -1:
                return t
        return -1
    if target == '0000':
        return 0
    s = set(deadends)
    if '0000' in s:
        return -1
    return bfs()
"-----------------"
test()

