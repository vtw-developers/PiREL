
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["I speak Goat Latin"]
    # output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    ,
    # example 2
    ["The quick brown fox jumped over the lazy dog"]
    # output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### toGoatLatin 
from typing import *
def f_gold(sentence: str) -> str:
    ans = []
    for i, word in enumerate(sentence.split()):
        if word.lower()[0] not in ['a', 'e', 'i', 'o', 'u']:
            word = word[1:] + word[0]
        word += 'ma'
        word += 'a' * (i + 1)
        ans.append(word)
    return ' '.join(ans)
"-----------------"
test()

