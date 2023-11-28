from L1816_TruncateSentence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["Hello how are you Contestant", 4]
    # output: "Hello how are you"
    # EXPLANATION:  The words in s are ["Hello", "how" "are", "you", "Contestant"]. The first 4 words are ["Hello", "how", "are", "you"]. Hence, you should return "Hello how are you".
    ,
    # example 2
    ["What is the solution to this problem", 4]
    # output: "What is the solution"
    # EXPLANATION:  The words in s are ["What", "is" "the", "solution", "to", "this", "problem"]. The first 4 words are ["What", "is", "the", "solution"]. Hence, you should return "What is the solution".
    ,
    # example 3
    ["chopper is not a tanuki", 5]
    # output: "chopper is not a tanuki"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
