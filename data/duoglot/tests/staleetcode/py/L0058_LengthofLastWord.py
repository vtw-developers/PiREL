
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["Hello World"]
    # output: 5
    # EXPLANATION:  The last word is "World" with length 5.
    ,
    # example 2
    ["   fly me   to   the moon  "]
    # output: 4
    # EXPLANATION:  The last word is "moon" with length 4.
    ,
    # example 3
    ["luffy is still joyboy"]
    # output: 6
    # EXPLANATION:  The last word is "joyboy" with length 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lengthOfLastWord 
from typing import *
def f_gold(s: str) -> int:
    last_word_length = 0
    meet_word = False
    for i in range(len(s) - 1, -1, -1):
        ch = ord(s[i])
        if ch >= 65 and ch <= 122:
            meet_word = True
            last_word_length += 1
        elif meet_word:
            break
    return last_word_length
"-----------------"
test()

