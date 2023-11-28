from L2047_NumberofValidWordsinaSentence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["cat and  dog"]
    # output: 3
    # EXPLANATION:  The valid words in the sentence are "cat", "and", and "dog".
    ,
    # example 2
    ["!this  1-s b8d!"]
    # output: 0
    # EXPLANATION:  There are no valid words in the sentence. "!this" is invalid because it starts with a punctuation mark. "1-s" and "b8d" are invalid because they contain digits.
    ,
    # example 3
    ["alice and  bob are playing stone-game10"]
    # output: 5
    # EXPLANATION:  The valid words in the sentence are "alice", "and", "bob", "are", and "playing". "stone-game10" is invalid because it contains digits.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
