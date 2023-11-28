
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"]
    # output: 1
    ,
    # example 2
    [["practice", "makes", "perfect", "coding", "makes"], "makes", "makes"]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestWordDistance 
from typing import *
def f_gold(wordsDict: List[str], word1: str, word2: str) -> int:
    i1 = i2 = -1
    shortest_distance = len(wordsDict)
    same = word1 == word2
    for i in range(len(wordsDict)):
        if same:
            if word1 == wordsDict[i]:
                if i1 != -1:
                    shortest_distance = min(shortest_distance, i - i1)
                i1 = i
        else:
            if word1 == wordsDict[i]:
                i1 = i
            if word2 == wordsDict[i]:
                i2 = i
            if i1 != -1 and i2 != -1:
                shortest_distance = min(shortest_distance, abs(i1 - i2))
    return shortest_distance
"-----------------"
test()

