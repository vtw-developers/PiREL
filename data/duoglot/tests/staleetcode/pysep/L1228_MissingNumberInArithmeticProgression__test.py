from L1228_MissingNumberInArithmeticProgression import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 7, 11, 13]]
    # output: 9
    # EXPLANATION:  The previous array was [5,7,<strong>9</strong>,11,13].
    ,
    # example 2
    [[15, 13, 12]]
    # output: 14
    # EXPLANATION:  The previous array was [15,<strong>14</strong>,13,12].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
