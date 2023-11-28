
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 1]]
    # output: 3
    # EXPLANATION:  We can pick from all 3 trees.
    ,
    # example 2
    [[0, 1, 2, 2]]
    # output: 3
    # EXPLANATION:  We can pick from trees [1,2,2]. If we had started at the first tree, we would only pick from trees [0,1].
    ,
    # example 3
    [[1, 2, 3, 2, 2]]
    # output: 4
    # EXPLANATION:  We can pick from trees [2,3,2,2]. If we had started at the first tree, we would only pick from trees [1,2].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### totalFruit 
from collections import Counter
from typing import *
def f_gold(tree: List[int]) -> int:
    counter = Counter()
    i = res = 0
    for j, type in enumerate(tree):
        counter[type] += 1
        while len(counter) > 2:
            counter[tree[i]] -= 1
            if counter[tree[i]] == 0:
                counter.pop(tree[i])
            i += 1
        res = max(res, j - i + 1)
    return res
"-----------------"
test()

