from L0231_PowerofTwo import f_gold

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
    # output: true
    # EXPLANATION: 2<sup>0</sup> = 1
    ,
    # example 2
    [16]
    # output: true
    # EXPLANATION: 2<sup>4</sup> = 16
    ,
    # example 3
    [3]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
