
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
    # output: 5
    # EXPLANATION:  One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    ,
    # example 2
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]
    # output: 0
    # EXPLANATION:  The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### ladderLength 
from collections import deque
from typing import *
def f_gold(beginWord: str, endWord: str, wordList: List[str]) -> int:
    def extend(m1, m2, q):
        for _ in range(len(q)):
            s = q.popleft()
            step = m1[s]
            s = list(s)
            for i in range(len(s)):
                ch = s[i]
                for j in range(26):
                    s[i] = chr(ord('a') + j)
                    t = ''.join(s)
                    if t in m1 or t not in words:
                        continue
                    if t in m2:
                        return step + 1 + m2[t]
                    m1[t] = step + 1
                    q.append(t)
                s[i] = ch
        return -1
    words = set(wordList)
    if endWord not in words:
        return 0
    q1, q2 = deque([beginWord]), deque([endWord])
    m1, m2 = {beginWord: 0}, {endWord: 0}
    while q1 and q2:
        t = extend(m1, m2, q1) if len(q1) <= len(q2) else extend(m2, m1, q2)
        if t != -1:
            return t + 1
    return 0
"-----------------"
test()

