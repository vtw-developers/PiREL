
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["My name is Haley", "My Haley"]
    # output: true
    # EXPLANATION:  sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
    ,
    # example 2
    ["of", "A lot of words"]
    # output: false
    # EXPLANATION: No single sentence can be inserted inside one of the sentences to make it equal to the other.
    ,
    # example 3
    ["Eating right now", "Eating"]
    # output: true
    # EXPLANATION:  sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
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
def f_gold(sentence1: str, sentence2: str) -> bool:
    if sentence1 == sentence2:
        return True
    n1, n2 = len(sentence1), len(sentence2)
    if n1 == n2:
        return False
    if n1 < n2:
        sentence1, sentence2 = sentence2, sentence1
    words1, words2 = sentence1.split(), sentence2.split()
    i = j = 0
    n1, n2 = len(words1), len(words2)
    while i < n2 and words1[i] == words2[i]:
        i += 1
    if i == n2:
        return True
    while j < n2 and words1[n1 - 1 - j] == words2[n2 - 1 - j]:
        j += 1
    return j == n2 or i + j == n2
"-----------------"
test()

