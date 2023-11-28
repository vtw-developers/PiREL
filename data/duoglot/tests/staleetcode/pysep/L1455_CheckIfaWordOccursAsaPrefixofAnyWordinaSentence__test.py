from L1455_CheckIfaWordOccursAsaPrefixofAnyWordinaSentence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["i love eating burger", "burg"]
    # output: 4
    # EXPLANATION:  "burg" is prefix of "burger" which is the 4th word in the sentence.
    ,
    # example 2
    ["this problem is an easy problem", "pro"]
    # output: 2
    # EXPLANATION:  "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
    ,
    # example 3
    ["i am tired", "you"]
    # output: -1
    # EXPLANATION:  "you" is not a prefix of any word in the sentence.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
