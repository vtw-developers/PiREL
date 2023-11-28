from L0306_AdditiveNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["112358"]
    # output: true
    # EXPLANATION:   The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.  1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
    ,
    # example 2
    ["199100199"]
    # output: true
    # EXPLANATION:   The additive sequence is: 1, 99, 100, 199.  1 + 99 = 100, 99 + 100 = 199
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
