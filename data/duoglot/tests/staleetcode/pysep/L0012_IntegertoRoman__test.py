from L0012_IntegertoRoman import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: "III"
    # EXPLANATION:  3 is represented as 3 ones.
    ,
    # example 2
    [58]
    # output: "LVIII"
    # EXPLANATION:  L = 50, V = 5, III = 3.
    ,
    # example 3
    [1994]
    # output: "MCMXCIV"
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
