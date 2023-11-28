from L0734_SentenceSimilarity import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]]
    # output: true
    # EXPLANATION:  The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
    ,
    # example 2
    [["great"], ["great"], []]
    # output: true
    # EXPLANATION:  A word is similar to itself.
    ,
    # example 3
    [["great"], ["doubleplus", "good"], [["great", "doubleplus"]]]
    # output: false
    # EXPLANATION:  As they don't have the same length, we return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
