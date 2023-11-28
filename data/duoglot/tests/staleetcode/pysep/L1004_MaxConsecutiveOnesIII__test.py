from L1004_MaxConsecutiveOnesIII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2]
    # output: 6
    # EXPLANATION:  [1,1,1,0,0,<u><strong>1</strong>,1,1,1,1,<strong>1</strong></u>] Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    ,
    # example 2
    [[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3]
    # output: 10
    # EXPLANATION:  [0,0,<u>1,1,<strong>1</strong>,<strong>1</strong>,1,1,1,<strong>1</strong>,1,1</u>,0,0,0,1,1,1,1] Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
