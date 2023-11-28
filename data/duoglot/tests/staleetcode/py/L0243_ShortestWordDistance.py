
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"]
    # output: 3
    ,
    # example 2
    [["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestDistance 
from typing import *
def f_gold(wordsDict: List[str], word1: str, word2: str) -> int:
    i1 = i2 = -1
    shortest_distance = len(wordsDict)
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            i1 = i
        elif wordsDict[i] == word2:
            i2 = i
        if i1 != -1 and i2 != -1:
            shortest_distance = min(shortest_distance, abs(i1 - i2))
    return shortest_distance
"-----------------"
test()

