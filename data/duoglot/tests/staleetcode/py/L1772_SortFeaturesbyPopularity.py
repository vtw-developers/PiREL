
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["cooler", "lock", "touch"], ["i like cooler cooler", "lock touch cool", "locker like touch"]]
    # output: ["touch","cooler","lock"]
    # EXPLANATION:  appearances("cooler") = 1, appearances("lock") = 1, appearances("touch") = 2. Since "cooler" and "lock" both had 1 appearance, "cooler" comes first because "cooler" came first in the features array.
    ,
    # example 2
    [["a", "aa", "b", "c"], ["a", "a aa", "a a a a a", "b a"]]
    # output: ["a","aa","b","c"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortFeatures 
from collections import Counter
from typing import *
def f_gold(features: List[str], responses: List[str]) -> List[str]:
    feature_set = set(features)
    counter = Counter()
    for resp in responses:
        for feat in set(resp.split(' ')):
            if feat in feature_set:
                counter[feat] += 1
    order = {feat: i for i, feat in enumerate(features)}
    return sorted(features, key=lambda feat: (-counter[feat], order[feat]))
"-----------------"
test()

