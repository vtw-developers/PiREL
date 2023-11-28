from L1813_SentenceSimilarityIII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["My name is Haley", "My Haley"]
    # output: true
    # EXPLANATION:  sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
    ,
    # example 2
    ["of", "A lot of words"]
    # output: false
    # EXPLANATION: No single sentence can be inserted inside one of the sentences to make it equal to the other.
    ,
    # example 3
    ["Eating right now", "Eating"]
    # output: true
    # EXPLANATION:  sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
