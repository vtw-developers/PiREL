
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"]
    # output: ["mee","aqq"]
    # EXPLANATION:  "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.  "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
    ,
    # example 2
    [["a", "b", "c"], "a"]
    # output: ["a","b","c"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findAndReplacePattern 
from typing import *
def f_gold(words: List[str], pattern: str) -> List[str]:
    def match(s, t):
        m1, m2 = [0] * 128, [0] * 128
        for i, (a, b) in enumerate(zip(s, t), 1):
            if m1[ord(a)] != m2[ord(b)]:
                return False
            m1[ord(a)] = m2[ord(b)] = i
        return True
    return [word for word in words if match(word, pattern)]
"-----------------"
test()

