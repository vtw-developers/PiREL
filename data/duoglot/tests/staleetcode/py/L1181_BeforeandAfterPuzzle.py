
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["writing code", "code rocks"]]
    # output: ["writing code rocks"]
    ,
    # example 2
    [["mission statement", "a quick bite to eat", "a chip off the old block", "chocolate bar", "mission impossible", "a man on a mission", "block party", "eat my words", "bar of soap"]]
    # output: ["a chip off the old block party",         "a man on a mission impossible",         "a man on a mission statement",         "a quick bite to eat my words",         "chocolate bar of soap"]
    ,
    # example 3
    [["a", "b", "a"]]
    # output: ["a"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### beforeAndAfterPuzzles 
from collections import defaultdict
from typing import *
def f_gold(phrases: List[str]) -> List[str]:
    same_first_word = defaultdict(set)
    for i, phrase in enumerate(phrases):
        same_first_word[phrase.split()[0]].add(i)
    res = set()
    for i, phrase in enumerate(phrases):
        words = phrase.split()
        last_word = words[-1]
        if last_word in same_first_word:
            for j in same_first_word[last_word]:
                if i != j:
                    res.add(' '.join(words[:-1] + phrases[j].split()))
    return sorted(list(res))
"-----------------"
test()

