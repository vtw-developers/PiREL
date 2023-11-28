from L1554_StringsDifferbyOneCharacter import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abcd", "acbd", "aacd"]]
    # output: true
    # EXPLANATION:  Strings "a<strong>b</strong>cd" and "a<strong>a</strong>cd" differ only by one character in the index 1.
    ,
    # example 2
    [["ab", "cd", "yz"]]
    # output: false
    ,
    # example 3
    [["abcd", "cccc", "abyd", "abab"]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
