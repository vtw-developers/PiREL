
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]]
    # output: true
    # EXPLANATION:  The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
    ,
    # example 2
    [["great"], ["great"], []]
    # output: true
    # EXPLANATION:  A word is similar to itself.
    ,
    # example 3
    [["great"], ["doubleplus", "good"], [["great", "doubleplus"]]]
    # output: false
    # EXPLANATION:  As they don't have the same length, we return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### areSentencesSimilar 
from typing import *
def f_gold(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
) -> bool:
    if len(sentence1) != len(sentence2):
        return False
    pairs = {(word1, word2) for word1, word2 in similarPairs}
    for i in range(len(sentence1)):
        similar = (
            (sentence1[i], sentence2[i]) in pairs
            or (sentence2[i], sentence1[i]) in pairs
            or sentence1[i] == sentence2[i]
        )
        if not similar:
            return False
    return True
"-----------------"
test()

