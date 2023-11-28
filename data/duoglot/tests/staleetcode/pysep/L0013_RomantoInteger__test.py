from L0013_RomantoInteger import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["III"]
    # output: 3
    # EXPLANATION:  III = 3.
    ,
    # example 2
    ["LVIII"]
    # output: 58
    # EXPLANATION:  L = 50, V= 5, III = 3.
    ,
    # example 3
    ["MCMXCIV"]
    # output: 1994
    # EXPLANATION:  M = 1000, CM = 900, XC = 90 and IV = 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
