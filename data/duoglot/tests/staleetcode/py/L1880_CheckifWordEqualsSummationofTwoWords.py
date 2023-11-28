
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["acb", "cba", "cdb"]
    # output: true
    # EXPLANATION:  The numerical value of firstWord is "acb" -> "021" -> 21. The numerical value of secondWord is "cba" -> "210" -> 210. The numerical value of targetWord is "cdb" -> "231" -> 231. We return true because 21 + 210 == 231.
    ,
    # example 2
    ["aaa", "a", "aab"]
    # output: false
    # EXPLANATION:   The numerical value of firstWord is "aaa" -> "000" -> 0. The numerical value of secondWord is "a" -> "0" -> 0. The numerical value of targetWord is "aab" -> "001" -> 1. We return false because 0 + 0 != 1.
    ,
    # example 3
    ["aaa", "a", "aaaa"]
    # output: true
    # EXPLANATION:   The numerical value of firstWord is "aaa" -> "000" -> 0. The numerical value of secondWord is "a" -> "0" -> 0. The numerical value of targetWord is "aaaa" -> "0000" -> 0. We return true because 0 + 0 == 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isSumEqual 
from typing import *
def f_gold(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def convert(word):
        res = 0
        for c in word:
            res *= 10
            res += ord(c) - ord('a')
        return res
    return convert(firstWord) + convert(secondWord) == convert(targetWord)
"-----------------"
test()

