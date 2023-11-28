from L0127_WordLadder import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
    # output: 5
    # EXPLANATION:  One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    ,
    # example 2
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]
    # output: 0
    # EXPLANATION:  The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
