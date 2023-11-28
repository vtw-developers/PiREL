
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4]
    # output: 6
    # EXPLANATION:  The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6. Notice that book number 2 does not have to be on the first shelf.
    ,
    # example 2
    [[[1, 3], [2, 4], [3, 2]], 6]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minHeightShelves 
from typing import *
def f_gold(books: List[List[int]], shelfWidth: int) -> int:
    n = len(books)
    dp = [0] * (n + 1)
    dp[1] = books[0][1]
    for i in range(2, n + 1):
        dp[i] = books[i - 1][1] + dp[i - 1]
        w, h = books[i - 1][0], books[i - 1][1]
        for j in range(i - 1, 0, -1):
            w += books[j - 1][0]
            if w > shelfWidth:
                break
            h = max(books[j - 1][1], h)
            dp[i] = min(dp[i], dp[j - 1] + h)
    return dp[n]
"-----------------"
test()

