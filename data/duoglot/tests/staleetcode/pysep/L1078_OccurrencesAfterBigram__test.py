from L1078_OccurrencesAfterBigram import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["alice is a good girl she is a good student", "a", "good"]
    # output: ["girl","student"]
    ,
    # example 2
    ["we will we will rock you", "we", "will"]
    # output: ["we","rock"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
