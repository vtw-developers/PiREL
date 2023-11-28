from L2114_MaximumNumberofWordsFoundinSentences import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["alice and bob love leetcode", "i think so too", "this is great thanks very much"]]
    # output: 6
    # EXPLANATION:   - The first sentence, "alice and bob love leetcode", has 5 words in total. - The second sentence, "i think so too", has 4 words in total. - The third sentence, "this is great thanks very much", has 6 words in total. Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
    ,
    # example 2
    [["please wait", "continue to fight", "continue to win"]]
    # output: 3
    # EXPLANATION:  It is possible that multiple sentences contain the same number of words.  In this example, the second and third sentences (underlined) have the same number of words.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
