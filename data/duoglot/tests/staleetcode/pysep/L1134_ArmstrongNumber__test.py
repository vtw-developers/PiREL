from L1134_ArmstrongNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [153]
    # output: true
    # EXPLANATION:  153 is a 3-digit number, and 153 = 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup>.
    ,
    # example 2
    [123]
    # output: false
    # EXPLANATION:  123 is a 3-digit number, and 123 != 1<sup>3</sup> + 2<sup>3</sup> + 3<sup>3</sup> = 36.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
