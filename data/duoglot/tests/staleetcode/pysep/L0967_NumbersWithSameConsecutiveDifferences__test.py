from L0967_NumbersWithSameConsecutiveDifferences import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 7]
    # output: [181,292,707,818,929]
    # EXPLANATION:  Note that 070 is not a valid number, because it has leading zeroes.
    ,
    # example 2
    [2, 1]
    # output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
