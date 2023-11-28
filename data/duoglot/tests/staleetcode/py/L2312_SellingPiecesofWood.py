
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 5, [[1, 4, 2], [2, 2, 7], [2, 1, 3]]]
    # output: 19
    # EXPLANATION:  The diagram above shows a possible scenario. It consists of: - 2 pieces of wood shaped 2 x 2, selling for a price of 2 * 7 = 14. - 1 piece of wood shaped 2 x 1, selling for a price of 1 * 3 = 3. - 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2. This obtains a total of 14 + 3 + 2 = 19 money earned. It can be shown that 19 is the maximum amount of money that can be earned.
    ,
    # example 2
    [4, 6, [[3, 2, 10], [1, 4, 2], [4, 1, 3]]]
    # output: 32
    # EXPLANATION:  The diagram above shows a possible scenario. It consists of: - 3 pieces of wood shaped 3 x 2, selling for a price of 3 * 10 = 30. - 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2. This obtains a total of 30 + 2 = 32 money earned. It can be shown that 32 is the maximum amount of money that can be earned. Notice that we cannot rotate the 1 x 4 piece of wood to obtain a 4 x 1 piece of wood.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sellingWood 
def cache(f): return f
from collections import defaultdict
from typing import *
def f_gold(m: int, n: int, prices: List[List[int]]) -> int:
    @cache
    def dfs(h, w):
        ans = d[h].get(w, 0)
        for i in range(1, h // 2 + 1):
            ans = max(ans, dfs(i, w) + dfs(h - i, w))
        for i in range(1, w // 2 + 1):
            ans = max(ans, dfs(h, i) + dfs(h, w - i))
        return ans
    d = defaultdict(dict)
    for h, w, p in prices:
        d[h][w] = p
    return dfs(m, n)
"-----------------"
test()

