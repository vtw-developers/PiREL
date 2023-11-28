
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]]
    # output: ["eat","oath"]
    ,
    # example 2
    [[["a", "b"], ["c", "d"]], ["abcb"]]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findWords 
from collections import Counter
from typing import *
def f_gold(board: List[List[str]], words: List[str]) -> List[str]:
    def check(word):
        cnt = Counter(word)
        return all(counter[c] >= i for c, i in cnt.items())
    def dfs(i, j, l, word):
        if l == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[l]:
            return False
        c = board[i][j]
        board[i][j] = '0'
        ans = False
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            ans = ans or dfs(x, y, l + 1, word)
        board[i][j] = c
        return ans
    def find(word):
        if not check(word):
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, word):
                    return True
        return False
    m, n = len(board), len(board[0])
    words = set(words)
    counter = Counter(c for b in board for c in b)
    return [word for word in words if find(word)]
"-----------------"
test()

