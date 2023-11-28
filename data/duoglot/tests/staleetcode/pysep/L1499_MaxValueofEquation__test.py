from L1499_MaxValueofEquation import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3], [2, 0], [5, 10], [6, -10]], 1]
    # output: 4
    # EXPLANATION:  The first two points satisfy the condition |x<sub>i</sub> - x<sub>j</sub>| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1. No other pairs satisfy the condition, so we return the max of 4 and 1.
    ,
    # example 2
    [[[0, 0], [3, 0], [9, 2]], 3]
    # output: 3
    # EXPLANATION: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
