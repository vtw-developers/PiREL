from L1220_CountVowelsPermutation import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 5
    # EXPLANATION:  All possible strings are: "a", "e", "i" , "o" and "u".
    ,
    # example 2
    [2]
    # output: 10
    # EXPLANATION:  All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
    ,
    # example 3
    [5]
    # output: 68
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
