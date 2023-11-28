
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["is2 sentence4 This1 a3"]
    # output: "This is a sentence"
    # EXPLANATION:  Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
    ,
    # example 2
    ["Myself2 Me1 I4 and3"]
    # output: "Me Myself and I"
    # EXPLANATION:  Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortSentence 
from typing import *
def f_gold(s: str) -> str:
    words = s.split(' ')
    arr = [None] * len(words)
    for word in words:
        idx = int(word[-1]) - 1
        arr[idx] = word[:-1]
    return ' '.join(arr)
"-----------------"
test()

