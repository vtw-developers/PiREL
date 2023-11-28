from L1309_DecryptStringfromAlphabettoIntegerMapping import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["10#11#12"]
    # output: "jkab"
    # EXPLANATION:  "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
    ,
    # example 2
    ["1326#"]
    # output: "acz"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
