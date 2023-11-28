from L1796_SecondLargestDigitinaString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["dfa12321afd"]
    # output: 2
    # EXPLANATION:  The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
    ,
    # example 2
    ["abc1111"]
    # output: -1
    # EXPLANATION:  The digits that appear in s are [1]. There is no second largest digit.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
