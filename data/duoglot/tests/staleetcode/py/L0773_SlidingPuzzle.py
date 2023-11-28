
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 0, 5]]]
    # output: 1
    # EXPLANATION:  Swap the 0 and the 5 in one move.
    ,
    # example 2
    [[[1, 2, 3], [5, 4, 0]]]
    # output: -1
    # EXPLANATION:  No number of moves will make the board solved.
    ,
    # example 3
    [[[4, 1, 2], [5, 0, 3]]]
    # output: 5
    # EXPLANATION:  5 is the smallest number of moves that solves the board. An example path: After move 0: [[4,1,2],[5,0,3]] After move 1: [[4,1,2],[0,5,3]] After move 2: [[0,1,2],[4,5,3]] After move 3: [[1,0,2],[4,5,3]] After move 4: [[1,2,0],[4,5,3]] After move 5: [[1,2,3],[4,5,0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### slidingPuzzle 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(board: List[List[int]]) -> int:
    m, n = 2, 3
    seq = []
    start, end = '', '123450'
    for i in range(m):
        for j in range(n):
            if board[i][j] != 0:
                seq.append(board[i][j])
            start += str(board[i][j])
    def check(seq):
        n = len(seq)
        cnt = sum(seq[i] > seq[j] for i in range(n) for j in range(i, n))
        return cnt % 2 == 0
    def f(s):
        ans = 0
        for i in range(m * n):
            if s[i] != '0':
                num = ord(s[i]) - ord('1')
                ans += abs(i // n - num // n) + abs(i % n - num % n)
        return ans
    if not check(seq):
        return -1
    q = [(f(start), start)]
    dist = {start: 0}
    while q:
        _, state = heappop(q)
        if state == end:
            return dist[state]
        p1 = state.index('0')
        i, j = p1 // n, p1 % n
        s = list(state)
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n:
                p2 = x * n + y
                s[p1], s[p2] = s[p2], s[p1]
                next = ''.join(s)
                s[p1], s[p2] = s[p2], s[p1]
                if next not in dist or dist[next] > dist[state] + 1:
                    dist[next] = dist[state] + 1
                    heappush(q, (dist[next] + f(next), next))
    return -1
"-----------------"
test()

