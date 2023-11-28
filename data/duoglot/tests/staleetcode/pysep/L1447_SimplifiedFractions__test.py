from L1447_SimplifiedFractions import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: ["1/2"]
    # EXPLANATION:  "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
    ,
    # example 2
    [3]
    # output: ["1/2","1/3","2/3"]
    ,
    # example 3
    [4]
    # output: ["1/2","1/3","1/4","2/3","3/4"]
    # EXPLANATION:  "2/4" is not a simplified fraction because it can be simplified to "1/2".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
