from L0202_HappyNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [19]
    # output: true
    # EXPLANATION:  1<sup>2</sup> + 9<sup>2</sup> = 82 8<sup>2</sup> + 2<sup>2</sup> = 68 6<sup>2</sup> + 8<sup>2</sup> = 100 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
    ,
    # example 2
    [2]
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
