from L1413_MinimumValuetoGetPositiveStepbyStepSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-3, 2, -3, 4, 2]]
    # output: 5
    # EXPLANATION: If you choose startValue = 4, in the third iteration your step by step sum is less than 1. <strong>step by step sum</strong> <strong>startValue = 4 | startValue = 5 | nums</strong>   (4 <strong>-3</strong> ) = 1  | (5 <strong>-3</strong> ) = 2    |  -3   (1 <strong>+2</strong> ) = 3  | (2 <strong>+2</strong> ) = 4    |   2   (3 <strong>-3</strong> ) = 0  | (4 <strong>-3</strong> ) = 1    |  -3   (0 <strong>+4</strong> ) = 4  | (1 <strong>+4</strong> ) = 5    |   4   (4 <strong>+2</strong> ) = 6  | (5 <strong>+2</strong> ) = 7    |   2
    ,
    # example 2
    [[1, 2]]
    # output: 1
    # EXPLANATION:  Minimum start value should be positive.
    ,
    # example 3
    [[1, -2, -3]]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
