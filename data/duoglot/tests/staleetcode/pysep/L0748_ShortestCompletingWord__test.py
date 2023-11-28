from L0748_ShortestCompletingWord import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1s3 PSt", ["step", "steps", "stripe", "stepple"]]
    # output: "steps"
    # EXPLANATION:  licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'. "step" contains 't' and 'p', but only contains 1 's'. "steps" contains 't', 'p', and both 's' characters. "stripe" is missing an 's'. "stepple" is missing an 's'. Since "steps" is the only word containing all the letters, that is the answer.
    ,
    # example 2
    ["1s3 456", ["looks", "pest", "stew", "show"]]
    # output: "pest"
    # EXPLANATION:  licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
