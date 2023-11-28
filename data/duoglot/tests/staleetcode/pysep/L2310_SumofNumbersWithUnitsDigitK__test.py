from L2310_SumofNumbersWithUnitsDigitK import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [58, 9]
    # output: 2
    # EXPLANATION:  One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9. Another valid set is [19,39]. It can be shown that 2 is the minimum possible size of a valid set.
    ,
    # example 2
    [37, 2]
    # output: -1
    # EXPLANATION:  It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.
    ,
    # example 3
    [0, 7]
    # output: 0
    # EXPLANATION:  The sum of an empty set is considered 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
