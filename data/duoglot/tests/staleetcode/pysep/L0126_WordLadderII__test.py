from L0126_WordLadderII import f_gold

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
    # output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    # EXPLANATION:  There are 2 shortest transformation sequences: "hit" -> "hot" -> "dot" -> "dog" -> "cog" "hit" -> "hot" -> "lot" -> "log" -> "cog"
    ,
    # example 2
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]
    # output: []
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
