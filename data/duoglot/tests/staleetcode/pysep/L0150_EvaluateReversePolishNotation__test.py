from L0150_EvaluateReversePolishNotation import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["2", "1", "+", "3", "*"]]
    # output: 9
    # EXPLANATION:  ((2 + 1) * 3) = 9
    ,
    # example 2
    [["4", "13", "5", "/", "+"]]
    # output: 6
    # EXPLANATION:  (4 + (13 / 5)) = 6
    ,
    # example 3
    [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
    # output: 22
    # EXPLANATION:  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = ((10 * (6 / (12 * -11))) + 17) + 5 = ((10 * (6 / -132)) + 17) + 5 = ((10 * 0) + 17) + 5 = (0 + 17) + 5 = 17 + 5 = 22
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
